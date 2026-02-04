"""Temporal PredQL converter module for time-series queries."""

import pandas as pd
from predql.base import Database, Table

from predql.converter.converter import Converter
from predql.converter.utils import build_aggr_func, get_div_line


class TConverter(Converter):
    r"""Temporal PredQL converter class for temporal conversion PredQL -> SQL.

    Converts temporal (time-series) PredQL queries into SQL queries.\
    Extends the base ConverterPredQL class with concrete implementations\
    for temporal prediction tasks with time window support.
    """

    def __init__(self,
                 db         : Database,
                 timestamps : "pd.Series[pd.Timestamp]") -> None:
        r"""Initializes a temporal PredQL converter with timestamp support.

        Args:
            db (Database): Database object containing the tables.
            timestamps (pd.Series[pd.Timestamp]): Initial time points for predictions.

        Returns:
            out (None):
        """
        super().__init__(db)

        # store timestamps for temporal prediction
        self.timestamps = timestamps
        # create DataFrame with timestamp column for temporal operations
        timestamp_df = pd.DataFrame({"timestamp" : self.timestamps})
        # register timestamp_df in DuckDB for SQL queries
        self.conn.register("timestamp_df", timestamp_df)

        self.tmp = True


    def convert(self,
                predql_query : str) -> Table:
        r"""Converts the temporal PredQL query string into an executable SQL query.

        Returns the result as a *`Table`* object.

        Args:
            predql_query (str): The PredQL query string to be converted and executed.

        Returns:
            out (Table): The *`Table`* object containing the result of the executed SQL query,\
                    with columns (*fk*, *timestamp*, *label*) corresponding to the translated PredQL query output.
        """
        # parse PredQL query into dictionary
        query_dict = self.parse_query(predql_query)

        # check FOR EACH
        for_each_dict = query_dict["ForEach"].value
        # extract parent table name
        ptable = for_each_dict["Table"].value
        # extract primary key column name
        ppk = for_each_dict["Column"].value

        # check if FOR_EACH has WHERE clause for filtering
        for_each_query = None
        # if exists -> build for_each_query
        # otherwise -> for_each_query remains None
        if where := for_each_dict["Where"]:
            where_dict = where.value
            for_each_query = self.build_expr(where_dict["Expr"].value, ptable, ppk)

        # build PREDICT query
        predict_dict = query_dict["Predict"].value
        sql_query = self.build_predict(predict_dict, ptable, ppk, for_each_query)

        # check ASSUMING clause to filter predictions
        if assuming := query_dict["Assuming"]:
            assuming_dict = assuming.value
            sql_query = self.build_assuming(assuming_dict, ptable, ppk, sql_query)

        # handle WHERE conditions from PREDICT clause
        # NOTE: will be moved to build_predict in future versions(for nested WHERE in aggregation)
        if predict_aggr := predict_dict["Aggregation"]:
            predict_aggr_dict = predict_aggr.value
            # if WHERE exists in aggregation -> apply additional filtering
            if predict_where := predict_aggr_dict["Where"]:
                predict_where_dict = predict_where.value
                sql_query = sql_query.replace("\n", "\n" + 4*" ") + "\n"

                help_query = self.build_expr(predict_where_dict["Expr"].value, ptable, ppk)
                help_query = help_query.replace("\n", "\n" + 4*" ") + "\n"

                sql_query = (
                     "SELECT\n"
                     "    sq.fk,\n"
                     "    sq.timestamp,\n"
                     "    sq.label\n"
                     "FROM\n"
                    f"    ({sql_query}) sq\n"
                     "JOIN\n"
                    f"    ({help_query}) hq\n"
                     "ON\n"
                     "    hq.fk = sq.fk\n"
                     "ORDER BY\n"
                     "    sq.timestamp ASC, sq.fk ASC" 
                )

        # add semicolon to end of SQL query
        sql_query = f"{sql_query}\n;"

        print(sql_query)

        # execute SQL query and return result as Table
        df = self.conn.sql(sql_query).df
        return Table(
            df=df,
            fkey_col_to_pkey_table=None,
            pkey_col=None,
            time_col="timestamp",  # mark timestamp as the time column
            )


    def build_assuming(self,
                       query_dict    : dict,
                       ptable        : str,
                       ppk           : str,
                       predict_query : str) -> str:
        r"""Restricts a temporal prediction query using an ASSUMING expression.

        Filters prediction results to keep only rows where the ASSUMING condition is true.
        Works by joining the prediction results with the ASSUMING expression on both fk and timestamp,
        preserving the label column only for matching rows.

        Args:
            query_dict (dict): Parsed dictionary of the ASSUMING clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            predict_query (str): The SQL subquery for the PREDICT part (fk, timestamp, label).

        Returns:
            assuming_query (str): The SQL query filtering predictions using ASSUMING with temporal constraints.
        """
        # build assuming expression
        expr_dict = query_dict["Expr"].value
        expr_query = self.build_expr(expr_dict, ptable, ppk)
        expr_query = expr_query.replace("\n", "\n" + 4*" ") + "\n"

        # create division markers for formatted output
        div_line_ass1 = get_div_line("ASSUMING_START")
        div_line_ass2 = get_div_line("ASSUMING_END")
        div_line_help1 = get_div_line("HELP_PART_START")
        div_line_help2 = get_div_line("HELP_PART_END")

        # build ASSUMING query with temporal join
        predict_query = predict_query.replace("\n", "\n" + 4*" ") + "\n"
        assuming_query = (
            f"{div_line_ass1}\n"
             "SELECT\n"
            f"    help.{ppk} AS fk,\n"
             "    help.timestamp,\n"
             "    help.label\n"
             "FROM\n"
             "    (\n"
            f"{div_line_help1}\n"
             "    SELECT\n"
            f"        parent.{ppk},\n"
             "        predict.timestamp,\n"
             "        predict.label\n"
             "    FROM\n"
            f"        {ptable} parent\n"
             "    JOIN\n"
            f"        ({predict_query}) predict\n"
             "    ON\n"
            f"        predict.fk = parent.{ppk}\n"
            f"{div_line_help2}\n"
             "    ) help\n"
             "JOIN\n"
            f"    ({expr_query}) expr\n"
             "ON\n"
            f"    expr.fk = help.{ppk}\n"
             "AND\n"
             "    expr.timestamp = help.timestamp\n"
             "ORDER BY\n"
            f"    help.timestamp ASC, help.{ppk} ASC\n"
            f"{div_line_ass2}"
        )

        return assuming_query


    def build_predict(self,
                      query_dict     : dict,
                      ptable         : str,
                      ppk            : str,
                      for_each_query : str) -> str:
        r"""Builds the SQL query for the PREDICT clause in temporal conversion.

        Handles temporal prediction logic by cross-joining with prediction timestamps and
        implementing different label generation strategies based on prediction type.

        Args:
            query_dict (dict): Parsed dictionary of the PREDICT clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            for_each_query (str): SQL subquery from FOR_EACH WHERE (can be None).

        Returns:
            predict_query (str): SQL subquery returning (fk, timestamp, label) triples.
        """
        # check predict type, build main_query and label_query accordingly
        # aggregation / expr
        pred_type = query_dict["PredType"]
        if pred_type == "aggregation":
            main_query = self.build_aggregation(query_dict["Aggregation"].value, ptable, ppk)

            # determine label extraction logic based on modifiers
            if query_dict["Classify"]:
                # CLASSIFY: use aggregated value directly
                label_query = "main.comp_col"
            elif query_dict["RankTop"]:
                # RANK_TOP K: keep only top K elements from aggregation
                K = int(query_dict["K"].value)
                label_query = (
                     "CASE\n"
                    f"    WHEN ARRAY_LENGTH(main.comp_col) > {K} THEN main.comp_col[1:{K}]\n"
                     "    ELSE main.comp_col\n"
                     "END"
                )
            else:
                # default: use full aggregated value
                label_query = "main.comp_col"
        elif pred_type == "expr":
            main_query = self.build_expr(query_dict["Expr"].value, ptable, ppk)
            
            label_query = (
                "CASE\n"
                "    WHEN main.fk IS NOT NULL THEN TRUE\n"
                "    ELSE FALSE\n"
                "END"
            )
        else:
            raise ValueError(f"Unknown predict type: {pred_type}")
        main_query = main_query.replace("\n", "\n" + 4*" ") + "\n"
        label_query = label_query.replace("\n", "\n" + 4*" ") + "\n"

        # create division markers for formatted output
        div_line_pred1 = get_div_line("PREDICT_START")
        div_line_pred2 = get_div_line("PREDICT_END")
        div_line_help1 = get_div_line("HELP_PART_START")
        div_line_help2 = get_div_line("HELP_PART_END")

        # build final predict query depending on FOR EACH WHERE existence
        if for_each_query:
            for_each_query = for_each_query.replace("\n", "\n" + 4*" ") + "\n"
            predict_query = (
                f"{div_line_pred1}\n"
                 "SELECT\n"
                f"    help.{ppk} AS fk,\n"
                 "    help.timestamp,\n"
                f"    {label_query} AS label\n"
                 "FROM\n"
                 "    (\n"
                f"{div_line_help1}\n"
                 "    SELECT\n"
                f"        parent.{ppk},\n"
                 "        for_each.timestamp,\n"
                 "    FROM\n"
                f"        {ptable} parent\n"
                 "    JOIN\n"
                f"        ({for_each_query}) for_each\n"
                 "    ON\n"
                f"        for_each.fk = parent.{ppk}\n"
                f"{div_line_help2}\n"
                 "    ) help\n"
                 "LEFT JOIN\n"
                f"    ({main_query}) main\n"
                 "ON\n"
                f"    main.fk = help.{ppk}\n"
                 "AND\n"
                 "    main.timestamp = help.timestamp\n"
                 "ORDER BY\n"
                f"    help.timestamp ASC, help.{ppk} ASC\n"
                f"{div_line_pred2}"
            )
        else:
            predict_query = (
                f"{div_line_pred1}\n"
                 "SELECT\n"
                f"    parent.{ppk} AS fk,\n"
                 "    time.timestamp AS timestamp,\n"
                f"    {label_query} AS label\n"
                 "FROM\n"
                f"    {ptable} parent\n"
                 "CROSS JOIN\n"
                 "    timestamp_df time\n"
                 "LEFT JOIN\n"
                f"    ({main_query}) main\n"
                 "ON\n"
                f"    main.fk = parent.{ppk}\n"
                 "AND\n"
                 "    main.timestamp = time.timestamp\n"
                 "ORDER BY\n"
                f"    time.timestamp ASC, parent.{ppk} ASC\n"
                f"{div_line_pred2}"
            )

        return predict_query


    def build_expr(self,
                   expr_dict : dict,
                   ptable    : str,
                   ppk       : str) -> str:
        r"""Recursively builds a SQL query for a logical expression tree.

        Converts nested boolean expressions (from WHERE or ASSUMING clauses) into SQL.
        Combines sub-expressions using UNION (for OR) or INTERSECT (for AND) operations
        to return a set of (foreign key, timestamp) pairs where the expression evaluates to true.

        Args:
            expr_dict (dict): Parsed dictionary of the expression (can contain 'Op',
                'Left', 'Right' keys or a single condition).
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            expr_query (str): SQL query returning (foreign key, timestamps pairs) where the expression is true.
        """
        # create division markers for formatted output
        div_line_expr1 = get_div_line("EXPR_START")
        div_line_expr2 = get_div_line("EXPR_END")

        # if expression is composite (AND/OR) -> recursively build left and right sub-expressions
        # otherwise -> build single condition expression
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            # build left expession
            left_expr = self.build_expr(expr_dict["Left"], ptable, ppk)
            left_expr = left_expr.replace("\n", "\n" + 4*" ") + "\n"
            # build right expression
            right_expr = self.build_expr(expr_dict["Right"], ptable, ppk)
            right_expr = right_expr.replace("\n", "\n" + 4*" ") + "\n"

            # check operation and convert to SQL format for tables
            op = expr_dict["Op"].value.lower()
            if op == "and":
                filt = "INTERSECT"
            elif op == "or":
                filt = "UNION"
            else:
                raise ValueError(f"Unknown operation in expression: {op}")

            expr_query = (
                f"{div_line_expr1}\n"
                 "SELECT\n"
                 "    fk,\n"
                 "    timestamp\n"
                 "FROM\n"
                f"    ({left_expr}) left_expr\n"
                f"{filt}\n"
                 "SELECT\n"
                 "    fk,\n"
                 "    timestamp\n"
                 "FROM\n"
                f"    ({right_expr}) right_expr\n"
                f"{div_line_expr2}"
            )
        else:
            expr_query = self.build_condition(expr_dict.value, ptable, ppk)

        return expr_query


    def build_aggregation(self,
                          aggr_dict : dict,
                          ptable    : str,
                          ppk       : str) -> str:
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
        table = aggr_dict["Table"].value
        start = int(aggr_dict["Start"].value)
        end = int(aggr_dict["End"].value)
        # remove trailing 'S' from measure unit for SQL syntax
        measure_unit = aggr_dict["MeasureUnit"].value.upper().removesuffix("S")

        # create division markers for formatted output
        div_line_aggr1 = get_div_line("AGGREGATION_START")
        div_line_aggr2 = get_div_line("AGGREGATION_END")

        # find foreign key column in the aggregation table that links to parent table
        fk = self.find_fk(table, ptable, ppk)
        # find time column for temporal filtering
        time_column = self.find_time_column(table)
        # build SQL aggregation function with proper column references
        aggr_func = build_aggr_func(aggr_dict, fk, time_column, ppk)
        aggr = aggr_func("aggr_tbl").replace("\n", "\n" + 4*" ") + "\n"

        # build temporal aggregation query
        aggr_query = (
            f"{div_line_aggr1}\n"
             "SELECT\n"
            f"    parent.{ppk} AS fk,\n"
            f"    {aggr} AS comp_col,\n"
             "    time.timestamp AS timestamp\n"
             "FROM\n"
            f"    {ptable} parent\n"
             "CROSS JOIN\n"
             "    timestamp_df time\n"
             "LEFT JOIN\n"
            f"    {table} aggr_tbl\n"
             "ON\n"
            f"    aggr_tbl.{fk} = parent.{ppk}\n"
             "AND\n"
            f"    aggr_tbl.{time_column} >= time.timestamp + INTERVAL '{start} {measure_unit}'\n"
             "AND\n"
            f"    aggr_tbl.{time_column} < time.timestamp + INTERVAL '{end} {measure_unit}'\n"
             "GROUP BY\n"
            f"    time.timestamp, parent.{ppk}\n"
            f"{div_line_aggr2}" 
        )

        return aggr_query


    def find_time_column(self,
                         table_name : str) -> str:
        r"""Finds the name of the time column for a given table.

        Args:
            table_name (str): Name of the table whose time column is to be found.

        Returns:
            out (str): The name of the time column associated with the specified table.
        """
        table = self.db.table_dict[table_name]

        return table.time_col
