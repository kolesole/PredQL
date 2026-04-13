"""Temporal PredQL converter class for time-series queries."""

import sys

import pandas as pd

from predql.base import Database, Table
from predql.converter.converter import Converter
from predql.converter.utils import build_aggr_func, get_div_line
from predql.validator import TValidator


class TConverter(Converter):
    r"""Temporal PredQL converter class for temporal conversion PredQL -> SQL.

    Converts temporal (time-series) PredQL queries into SQL queries.
    Extends the base Converter class with concrete implementations
    for temporal prediction tasks with time window support.
    """

    def __init__(self, db: Database, timestamps: "pd.Series[pd.Timestamp]") -> None:
        r"""Initializes a temporal PredQL converter with timestamp support.

        Args:
            db (Database): Database object containing the tables.
            timestamps (pd.Series[pd.Timestamp]): Initial time points for predictions.

        Returns:
            out (None):
        """
        super().__init__(db)

        self.timestamps = timestamps
        # initialize temporal validator
        self.validator = TValidator(self.collector, self.db)

    def convert(self, predql_query: str, execute: bool = False) -> str | Table:
        r"""Converts the temporal PredQL query string into an executable SQL query.

        Args:
            predql_query (str): The PredQL query string to be converted and executed.
            execute (bool): If True, executes the generated SQL query and returns the result as a Table.

        Returns:
            out (str | Table): The *`Table`* object containing the result of the executed SQL query (if execute=True),
                    with columns (*fk*, *timestamp*, *label*) corresponding to the translated PredQL query output.
                    Otherawise, returns the generated SQL query string (if execute=False).
        """
        # check that prediction timestamps are provided and not empty
        if self.timestamps is None or self.timestamps.empty:
            self.collector.val_error(
                line=-1,
                column=-1,
                msg="For temporal conversion, prediction timestamps must be provided and cannot be empty"
            )
            sys.exit(1)
        
        # parse PredQL query into dictionary
        query_dict = self.parse_query(predql_query)
        query_dict = query_dict["QueryTmp"].value

        # build FOR EACH query
        for_each_dict = query_dict["ForEach"].value
        ptable, ppk, for_each_query = self.build_for_each(for_each_dict)

        # build PREDICT query
        predict_dict = query_dict["Predict"].value
        sql_query = self.build_predict(predict_dict, ptable, ppk, for_each_query)

        # build ASSUMING query if exists, using PREDICT query as base
        if assuming := query_dict["Assuming"]:
            assuming_dict = assuming.value
            sql_query = self.build_assuming_where(assuming_dict, ptable, ppk, sql_query, context="ASSUMING")

        # build WHERE query if exists, using PREDICT query as base
        if where := query_dict["Where"]:
            where_dict = where.value
            sql_query = self.build_assuming_where(where_dict, ptable, ppk, sql_query, context="WHERE")

        # create CTE for prediction timestamps
        timestamp_cte = f"{self._build_timestamp_cte()}\n"

        # fiter and add semicolon to end of SQL query
        label_fk = None
        select_clause = "*"
        filt = "label IS NOT NULL"
        if aggr := predict_dict["Aggregation"]:
            aggr_dict = aggr.value
            if aggr_dict["AggrType"].value.lower() == "list_distinct":
                filt = f"{filt} AND label != [NULL]"
                select_clause = "fk, timestamp, list_filter(label, x -> x IS NOT NULL) AS label"
                table, table_obj = self._find_table(aggr_dict["Table"].value)
                column = self._find_column(table, aggr_dict["Column"].value)

                label_fk = table if table_obj.pkey_col == column else table_obj.fkey_col_to_pkey_table.get(column)

        sql_query = (
            f"{timestamp_cte}SELECT\n    {select_clause}\nFROM\n  ({sql_query}\n)\nWHERE {filt}\nORDER BY timestamp ASC, fk ASC\n;\n"
        )

        if not execute:
            return sql_query

        # print(sql_query)

        self._register_db()
        ptable_orig, _ = self._find_table(ptable)

        # execute SQL query and return result as Table
        df = self.conn.sql(sql_query).df()
        fkey_col_to_pkey_table = {"fk": ptable_orig} # fk column in output table corresponds to pk of parent table
        if label_fk: # label column in output table corresponds to pk or fk of aggregation table
            fkey_col_to_pkey_table["label"] = label_fk # if aggregarion operation is LIST_DISTINCT

        return Table(
            df=df,
            fkey_col_to_pkey_table=fkey_col_to_pkey_table,
            pkey_col=None,
            time_col="timestamp",  # mark timestamp as the time column
        )

    def build_for_each(self, for_each_dict: dict) -> tuple[str, str, str]:
        r"""Builds a SQL query for the FOR EACH clause in temporal conversion.

        CROSS JOINS the parent table with timestamps.
        If the parent table has a time column, keeps only rows for which cur_timestamp >= time_col.

        Args:
            for_each_dict (dict): Parsed dictionary of the FOR EACH clause.

        Returns:
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            for_each_query (str): SQL subquery returning (*fk*, *timestamp*) pairs of
                    the parent table (optionally filtered).
        """
        # extract parent table and primary key column
        ptable = ptable_name = for_each_dict["Table"].value
        ppk = self._find_column(ptable, for_each_dict["Column"].value)

        # build static WHERE query if exists to filter parent table rows before prediction
        if where := for_each_dict["Where"]:
            ptable = self.build_stat_where(where.value, ptable, ppk)
            ptable = ptable.replace("\n", "\n" + 4 * " ") + "\n"
            ptable = f"({ptable})"

        # create division markers for formatted output
        div_line1 = get_div_line("FOR_EACH_START")
        div_line2 = get_div_line("FOR_EACH_END")

        # filter parent table rows based on time column
        # if exists -> time_col must be < timestamp
        # otherwise -> cross join with timestamps
        if time_col := self._find_time_column(ptable_name):
            for_each_query = (
                f"{div_line1}\n"
                "SELECT\n"
                f"    __PARENT__.{ppk} AS fk,\n"
                f"    __TIME__.timestamp AS timestamp\n"
                "FROM\n"
                f"    {ptable} __PARENT__\n"
                "JOIN\n"
                "    __TIMESTAMPS__ __TIME__\n"
                "ON\n"
                f"    __PARENT__.{time_col} <= __TIME__.timestamp\n"
                f"{div_line2}"
            )
        else:
            for_each_query = (
                f"{div_line1}\n"
                "SELECT\n"
                f"    __PARENT__.{ppk} AS fk,\n"
                f"    __TIME__.timestamp AS timestamp\n"
                "FROM\n"
                f"    {ptable} __PARENT__\n"
                "CROSS JOIN\n"
                "    __TIMESTAMPS__ __TIME__\n"
                f"{div_line2}"
            )

        # for_each_query = (
        #         f"{div_line1}\n"
        #          "SELECT\n"
        #         f"    __PARENT__.{ppk} AS fk,\n"
        #         f"    __TIME__.timestamp AS timestamp\n"
        #          "FROM\n"
        #         f"    {ptable} __PARENT__\n"
        #          "CROSS JOIN\n"
        #          "    __TIMESTAMPS__ __TIME__\n"
        #         f"{div_line2}"
        #     )

        return ptable_name, ppk, for_each_query

    def build_predict(self, predict_dict: dict, ptable: str, ppk: str, for_each_query: str) -> str:
        r"""Builds the SQL query for the PREDICT clause in temporal conversion.

        Handles temporal prediction logic by cross-joining with prediction timestamps and
        implementing different label generation strategies based on prediction type.

        Args:
            predict_dict (dict): Parsed dictionary of the PREDICT clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            for_each_query (str): SQL subquery from FOR_EACH WHERE (can be None).

        Returns:
            predict_query (str): SQL subquery returning (fk, timestamp, label) triples.
        """
        # check predict type, build main_query and label_query accordingly
        # aggregation / expr
        pred_type = predict_dict["PredType"]
        if pred_type == "aggregation":
            main_query = self.build_aggregation(predict_dict["Aggregation"].value, ptable, ppk)

            # determine label extraction logic based on modifiers
            if predict_dict["Classify"]:
                # CLASSIFY: use aggregated value directly
                label_query = "__MAIN__.comp_col"
            elif predict_dict["RankTop"]:
                # RANK_TOP K: keep only top K elements from aggregation
                k = int(predict_dict["K"].value)
                label_query = (
                    "CASE\n"
                    f"    WHEN ARRAY_LENGTH(__MAIN__.comp_col) > {k} THEN __MAIN__.comp_col[1:{k}]\n"
                    "    ELSE __MAIN__.comp_col\n"
                    "END"
                )
            else:
                # default: use full aggregated value
                label_query = "__MAIN__.comp_col"
        elif pred_type == "expr":
            main_query = self.build_expr(predict_dict["Expr"].value, ptable, ppk)

            label_query = "CASE\n    WHEN __MAIN__.fk IS NOT NULL THEN TRUE\n    ELSE FALSE\nEND"
        else:
            pass

        main_query = main_query.replace("\n", "\n" + 4 * " ") + "\n"
        label_query = label_query.replace("\n", "\n" + 4 * " ") + "\n"
        for_each_query = for_each_query.replace("\n", "\n" + 4 * " ") + "\n"

        # create division markers for formatted output
        div_line_pred1 = get_div_line("PREDICT_START")
        div_line_pred2 = get_div_line("PREDICT_END")
        div_line_help1 = get_div_line("HELP_PART_START")
        div_line_help2 = get_div_line("HELP_PART_END")

        # build final predict query
        predict_query = (
            f"{div_line_pred1}\n"
            "SELECT\n"
            f"    __HELP__.{ppk} AS fk,\n"
            "    __HELP__.timestamp,\n"
            f"    {label_query} AS label\n"
            "FROM\n"
            "    (\n"
            f"{div_line_help1}\n"
            "    SELECT\n"
            f"        __PARENT__.{ppk},\n"
            "        __FOR_EACH__.timestamp\n"
            "    FROM\n"
            f"        {ptable} __PARENT__\n"
            "    JOIN\n"
            f"        ({for_each_query}) __FOR_EACH__\n"
            "    ON\n"
            f"        __FOR_EACH__.fk = __PARENT__.{ppk}\n"
            f"{div_line_help2}\n"
            "    ) __HELP__\n"
            "LEFT JOIN\n"
            f"    ({main_query}) __MAIN__\n"
            "ON\n"
            f"    __MAIN__.fk = __HELP__.{ppk}\n"
            "AND\n"
            "    __MAIN__.timestamp = __HELP__.timestamp\n"
            f"{div_line_pred2}"
        )

        return predict_query

    def build_assuming_where(self, some_dict: dict, ptable: str, ppk: str, predict_query: str, context: str) -> str:
        r"""Restricts a temporal prediction query using an ASSUMING or WHERE expression.

        Filters prediction results to keep only rows where the ASSUMING or WHERE condition is true.
        Works by joining the prediction results with the ASSUMING or WHERE expression on both fk and timestamp,
        preserving the label column only for matching rows.

        Args:
            some_dict (dict): Parsed dictionary of the ASSUMING or WHERE clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            predict_query (str): The SQL subquery for the PREDICT part (*fk*, *timestamp*, *label*).
            context (str): String indicating the context of the filter ("ASSUMING" or "WHERE").

        Returns:
            assuming_query (str): The SQL query filtering predictions using ASSUMING with temporal constraints.
        """
        # build assuming expression
        expr_dict = some_dict["Expr"].value
        expr_query = self.build_expr(expr_dict, ptable, ppk)

        expr_query = expr_query.replace("\n", "\n" + 4 * " ") + "\n"
        predict_query = predict_query.replace("\n", "\n" + 4 * " ") + "\n"

        # create division markers for formatted output
        div_line_ass1 = get_div_line(f"{context}_START")
        div_line_ass2 = get_div_line(f"{context}_END")
        div_line_help1 = get_div_line("HELP_PART_START")
        div_line_help2 = get_div_line("HELP_PART_END")

        # build ASSUMING or WHERE query with temporal join
        assuming_where_query = (
            f"{div_line_ass1}\n"
            "SELECT\n"
            f"    __HELP__.{ppk} AS fk,\n"
            "    __HELP__.timestamp,\n"
            "    __HELP__.label\n"
            "FROM\n"
            "    (\n"
            f"{div_line_help1}\n"
            "    SELECT\n"
            f"        __PARENT__.{ppk},\n"
            "        __PREDICT__.timestamp,\n"
            "        __PREDICT__.label\n"
            "    FROM\n"
            f"        {ptable} __PARENT__\n"
            "    JOIN\n"
            f"        ({predict_query}) __PREDICT__\n"
            "    ON\n"
            f"        __PREDICT__.fk = __PARENT__.{ppk}\n"
            f"{div_line_help2}\n"
            "    ) __HELP__\n"
            "JOIN\n"
            f"    ({expr_query}) __EXPR__\n"
            "ON\n"
            f"    __EXPR__.fk = __HELP__.{ppk}\n"
            "AND\n"
            "    __EXPR__.timestamp = __HELP__.timestamp\n"
            f"{div_line_ass2}"
        )

        return assuming_where_query

    def build_expr(self, expr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Recursively builds a SQL query for a logical expression tree.

        Converts nested boolean expressions (from PREDICT, WHERE or ASSUMING clauses) into SQL.
        Combines sub-expressions using UNION (for OR) or INTERSECT (for AND) operations
        to return a set of (foreign key, timestamp) pairs where the expression evaluates to true.

        Args:
            expr_dict (dict): Parsed dictionary of the expression (can contain 'Op',
                'Left', 'Right' keys or a single condition).
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            expr_query (str): SQL query returning (*fk*, *timestamp*) pairs where the expression is true.
        """
        # create division markers for formatted output
        div_line_expr1 = get_div_line("EXPR_START")
        div_line_expr2 = get_div_line("EXPR_END")

        # if expression is composite (AND/OR) -> recursively build left and right sub-expressions
        # otherwise -> build single condition expression
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            # build left expession
            left_expr = self.build_expr(expr_dict["LeftExpr"], ptable, ppk)
            left_expr = left_expr.replace("\n", "\n" + 4 * " ") + "\n"
            # build right expression
            right_expr = self.build_expr(expr_dict["RightExpr"], ptable, ppk)
            right_expr = right_expr.replace("\n", "\n" + 4 * " ") + "\n"

            # check operation and convert to SQL format for tables
            op = expr_dict["Op"].value.lower()
            if op == "and":
                filt = "INTERSECT"
            elif op == "or":
                filt = "UNION"
            else:
                pass

            expr_query = (
                f"{div_line_expr1}\n"
                "SELECT\n"
                "    fk,\n"
                "    timestamp\n"
                "FROM\n"
                f"    ({left_expr}) __LEFT_EXPR__\n"
                f"{filt}\n"
                "SELECT\n"
                "    fk,\n"
                "    timestamp\n"
                "FROM\n"
                f"    ({right_expr}) __RIGHT_EXPR__\n"
                f"{div_line_expr2}"
            )
        else:
            expr_query = self.build_condition(expr_dict.value, ptable, ppk)

        return expr_query

    def build_aggregation(self, aggr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Builds the SQL query for a PredQL aggregation over a time window.

        Computes aggregations relative to prediction timestamps within a defined
        `[start, end)` time window.

        Args:
            aggr_dict (dict): Parsed aggregation dictionary with Table, Start, End, MeasureUnit.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            aggr_query (str): SQL query returning (fk, col_for_comp, timestamp) where col_for_comp is aggregated.
        """
        # extract aggregation parameters
        aggr_table = aggr_table_name = aggr_dict["Table"].value
        aggr_column = self._find_column(aggr_table, aggr_dict["Column"].value)
        start = float(aggr_dict["Start"].value)
        end = float(aggr_dict["End"].value)
        # remove trailing 'S' from measure unit for SQL syntax
        measure_unit = aggr_dict["MeasureUnit"].value.upper().removesuffix("S")

        # find foreign key column in the aggregation table that links to parent table
        fk = self._find_fk(aggr_table, ptable, ppk)
        # if not (fk := self._find_fk(aggr_table, ptable, ppk)):
        #     fk = self._find_pkey(aggr_table)
        # find time column for temporal filtering
        time_column = self._find_time_column(aggr_table)
        # build SQL aggregation function with proper column references
        aggr_dict["Column"].value = aggr_column
        aggr_func = build_aggr_func(aggr_dict, time_column)
        aggr = aggr_func("__AGGR_TBL__").replace("\n", "\n" + 4 * " ") + "\n"

        # build static WHERE query if exists to filter aggregation table rows before temporal aggregation
        if where := aggr_dict["Where"]:
            aggr_ppk = self._find_pkey(aggr_table)
            aggr_table = self.build_stat_where(where.value, aggr_table, aggr_ppk)
            aggr_table = aggr_table.replace("\n", "\n" + 4 * " ") + "\n"
            aggr_table = f"({aggr_table})"

        # build temporal filtering conditions based on start and end of time window
        start_query = ""
        if start != float("-inf"):
            start_query = (
                f"AND\n    __AGGR_TBL__.{time_column} > __TIME__.timestamp + INTERVAL '{start} {measure_unit}'\n"
            )

        end_query = ""
        if end != float("inf"):
            end_query = f"AND\n    __AGGR_TBL__.{time_column} <= __TIME__.timestamp + INTERVAL '{end} {measure_unit}'\n"

        # create division markers for formatted output
        div_line_aggr1 = get_div_line("AGGREGATION_START")
        div_line_aggr2 = get_div_line("AGGREGATION_END")

        # if aggregation column is a foreign key to another table with a time column ->
        # -> perform temporal join with that table to filter aggregation rows
        if (aggr_ptable := self._find_ptable(aggr_table_name, aggr_column)) and (
            aggr_ptable_time_col := self._find_time_column(aggr_ptable)
        ):
            aggr_ptable_pk = self._find_pkey(aggr_ptable)
            aggr_query = (
                f"{div_line_aggr1}\n"
                "SELECT\n"
                f"    __PARENT__.{ppk} AS fk,\n"
                f"    {aggr} AS comp_col,\n"
                "    __TIME__.timestamp AS timestamp\n"
                "FROM\n"
                f"    {ptable} __PARENT__\n"
                "CROSS JOIN\n"
                "    __TIMESTAMPS__ __TIME__\n"
                "LEFT JOIN\n"
                f"    {aggr_table} __AGGR_TBL__\n"
                "ON\n"
                f"    __AGGR_TBL__.{fk} = __PARENT__.{ppk}\n"
                f"{start_query}"
                f"{end_query}"
                "JOIN\n"
                f"    {aggr_ptable} __AGGR_PARENT__\n"
                "ON\n"
                f"    __AGGR_PARENT__.{aggr_ptable_pk} = __AGGR_TBL__.{aggr_column}\n"
                "AND\n"
                f"    __AGGR_PARENT__.{aggr_ptable_time_col} <= __TIME__.timestamp\n"
                "GROUP BY\n"
                f"    __TIME__.timestamp, __PARENT__.{ppk}\n"
                f"{div_line_aggr2}"
            )
            return aggr_query

        # build temporal aggregation query
        aggr_query = (
            f"{div_line_aggr1}\n"
            "SELECT\n"
            f"    __PARENT__.{ppk} AS fk,\n"
            f"    {aggr} AS comp_col,\n"
            "    __TIME__.timestamp AS timestamp\n"
            "FROM\n"
            f"    {ptable} __PARENT__\n"
            "CROSS JOIN\n"
            "    __TIMESTAMPS__ __TIME__\n"
            "LEFT JOIN\n"
            f"    {aggr_table} __AGGR_TBL__\n"
            "ON\n"
            f"    __AGGR_TBL__.{fk} = __PARENT__.{ppk}\n"
            f"{start_query}"
            f"{end_query}"
            "GROUP BY\n"
            f"    __TIME__.timestamp, __PARENT__.{ppk}\n"
            f"{div_line_aggr2}"
        )

        return aggr_query

    def set_timestamps(self, timestamps: "pd.Series[pd.Timestamp]") -> None:
        r"""Sets the prediction timestamps for the temporal converter.

        Args:
            timestamps (pd.Series[pd.Timestamp]): The new prediction timestamps to be used for conversion.

        Returns:
            out (None):
        """
        self.timestamps = timestamps

    ################## Helper methods ##################

    def _build_timestamp_cte(self) -> str:
        r"""Builds CTE (Common Table Expression) for the prediction timestamps.

        Returns:
            timestamp_cte (str): SQL CTE definition for the timestamps.
        """
        values = ",".join([f"(TIMESTAMP '{timestamp}')" for timestamp in self.timestamps])

        # create division markers for formatted output
        div_line_time1 = get_div_line("TIMESTAMP_CTE_START")
        div_line_time2 = get_div_line("TIMESTAMP_CTE_END")

        timestamp_cte = (
            f"{div_line_time1}\n"
            "WITH __TIMESTAMPS__ AS (\n"
            "    SELECT\n"
            "        *\n"
            "    FROM\n"
            f"        (VALUES {values}) AS tmp(timestamp)\n"
            ")\n"
            f"{div_line_time2}"
        )

        return timestamp_cte

    def _find_time_column(self, table_name: str) -> str:
        r"""Finds the name of the time column for a given table (case-insensitive).

        Args:
            table_name (str): Name of the table whose time column is to be found.

        Returns:
            out (str): The name of the time column associated with the specified table.
        """
        _, table = self._find_table(table_name)

        return table.time_col
