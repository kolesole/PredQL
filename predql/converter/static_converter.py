"""Static PredQL converter class for non-temporal queries."""

from predql.base import Database, Table
from predql.converter.converter import Converter
from predql.converter.utils import get_div_line
from predql.validator import SValidator


class SConverter(Converter):
    r"""Static PredQL converter class for static conversion PredQL -> SQL.

    Converts static (non-temporal) PredQL queries into SQL queries.
    Extends the base Converter class with concrete implementations
    for static prediction tasks.
    """

    def __init__(self, db: Database) -> None:
        r"""Initializes a static PredQL converter.

        Args:
            db (Database): Database object containing the tables.

        Returns:
            out (None):
        """
        super().__init__(db)
        # initialize static validator
        self.validator = SValidator(self.collector, self.db)

    def convert(self, predql_query: str, execute: bool = False) -> str | Table:
        r"""Converts the static PredQL query string into an executable SQL query.

        Args:
            predql_query (str): The PredQL query string to be converted and executed.
            execute (bool): If True, executes the generated SQL query and returns the result as a Table.

        Returns:
            out (str | Table): The *`Table`* object containing the result of the executed SQL query (if execute=True),
                    with columns (*fk*, *label*) corresponding to the translated PredQL query output.
                    Otherwise, returns the generated SQL query string (if execute=False).
        """
        # parse PredQL query into dictionary
        query_dict = self.parse_query(predql_query)
        query_dict = query_dict["QueryStat"].value

        # build FOR EACH query
        for_each_dict = query_dict["ForEach"].value
        ptable, ppk, for_each_query = self.build_for_each(for_each_dict)

        # build PREDICT query using FOR EACH query as base
        predict_dict = query_dict["Predict"].value
        sql_query = self.build_predict(predict_dict, ptable, ppk, for_each_query)

        # build WHERE query if exists, using PREDICT query as base
        if where := query_dict["Where"]:
            where_dict = where.value
            sql_query = self.build_where(where_dict, ptable, ppk, sql_query)

        # fiter and add semicolon to end of SQL query
        label_fk = None
        select_clause = "*"
        filt = "label IS NOT NULL"
        if aggr := predict_dict["Aggregation"]:
            aggr_dict = aggr.value
            if aggr_dict["AggrType"].value.lower() == "list_distinct":
                filt = f"{filt} AND label != [NULL]"
                select_clause = "fk, list_filter(label, x -> x IS NOT NULL) AS label"
                table, table_obj = self._find_table(aggr_dict["Table"].value)
                column = self._find_column(table, aggr_dict["Column"].value)

                label_fk = table if table_obj.pkey_col == column else table_obj.fkey_col_to_pkey_table.get(column)

        sql_query = f"SELECT\n    {select_clause}\nFROM\n  ({sql_query}\n)\nWHERE {filt}\nORDER BY fk ASC\n;\n"

        if not execute:
            return sql_query

        self._register_db()

        ptable_orig, _ = self._find_table(ptable)

        # execute SQL query and return result as Table
        df = self.conn.sql(sql_query).df()
        fkey_col_to_pkey_table = {"fk": ptable_orig} # fk column in output table corresponds to pk of parent table
        if label_fk:  # label column in output table corresponds to pk or fk of aggregation table
            fkey_col_to_pkey_table["label"] = label_fk # if aggregarion operation is LIST_DISTINCT

        return Table(
            df=df,
            fkey_col_to_pkey_table=fkey_col_to_pkey_table,
            pkey_col=None,
            time_col=None,
        )

    def build_for_each(self, for_each_dict: dict) -> tuple[str, str, str]:
        r"""Builds a SQL query for the FOR EACH clause in static conversion.

        Args:
            for_each_dict (dict): Parsed dictionary of the FOR EACH clause.

        Returns:
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            for_each_query (str): SQL subquery returning the foreign keys of
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

        # build final FOR EACH query
        for_each_query = f"{div_line1}\nSELECT\n    {ppk} AS fk\nFROM\n    {ptable}\n{div_line2}"

        return ptable_name, ppk, for_each_query

    def build_predict(self, query_dict: dict, ptable: str, ppk: str, for_each_query: str) -> str:
        r"""Builds a SQL query for the PREDICT clause in static conversion.

        Args:
            query_dict (dict): Parsed dictionary of the PREDICT clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            for_each_query (str): SQL subquery from the FOR_EACH WHERE clause, providing base fk column.

        Returns:
            predict_query (str): SQL subquery returning (fk, label) pairs.
        """
        # check predict type, build main_query and label_query accordingly
        # expr / id_dot_id
        pred_type = query_dict["PredType"]
        if pred_type == "aggregation":
            main_query = self.build_aggregation(query_dict["Aggregation"].value, ptable, ppk)
            label_query = "__MAIN__.comp_col"
        if pred_type == "expr":
            main_query = self.build_expr(query_dict["Expr"].value, ptable, ppk)
            label_query = "CASE\n    WHEN __MAIN__.fk IS NOT NULL THEN TRUE\n    ELSE FALSE\nEND"
        elif pred_type == "id_dot_id":
            main_query = self.build_id_dot_id(query_dict, ptable, ppk)
            label_query = "__MAIN__.comp_col"
        else:
            pass

        main_query = main_query.replace("\n", "\n" + 4 * " ") + "\n"
        label_query = label_query.replace("\n", "\n" + 4 * " ") + "\n"
        for_each_query = for_each_query.replace("\n", "\n" + 4 * " ") + "\n"

        # create division markers for formatted output
        div_line_pred1 = get_div_line("PREDICT_START")
        div_line_pred2 = get_div_line("PREDICT_END")

        # build final PREDICT query
        predict_query = (
            f"{div_line_pred1}\n"
            "SELECT\n"
            "    __FOR_EACH__.fk AS fk,\n"
            f"    {label_query} AS label\n"
            "FROM\n"
            f"    ({for_each_query}) __FOR_EACH__\n"
            "LEFT JOIN\n"
            f"    ({main_query}) __MAIN__\n"
            "ON\n"
            "    __MAIN__.fk = __FOR_EACH__.fk\n"
            f"{div_line_pred2}"
        )

        return predict_query

    def build_expr(self, expr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Builds a SQL query for a logical expression tree.

        Just uses existing *build_stat_expr* method from base *`Converter`* class.

        Args:
            expr_dict (dict): Parsed dictionary of the expression (can contain 'Op',
                'Left', 'Right' keys or a single condition).
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            expr_query (str): SQL query returning foreign keys where the expression is true.
        """
        expr_query = self.build_stat_expr(expr_dict, ptable, ppk)

        return expr_query

    def build_where(self, where_dict: dict, ptable: str, ppk: str, predict_query: str) -> str:
        r"""Builds a SQL query for the WHERE clause in static conversion.

        Combines the PREDICT query with the expression from the WHERE clause using JOIN
        to filter the predicted foreign keys based on the expression.

        Args:
            where_dict (dict): Parsed dictionary of the WHERE clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            predict_query (str): SQL query from the PREDICT clause, providing fk and label columns.

        Returns:
            where_query (str): SQL query returning (fk, label) pairs filtered by the WHERE expression.
        """
        expr_query = self.build_expr(where_dict["Expr"].value, ptable, ppk)
        expr_query = expr_query.replace("\n", "\n" + 4 * " ") + "\n"

        # create division markers for formatted output
        div_line1 = get_div_line("WHERE_START")
        div_line2 = get_div_line("WHERE_END")

        where_query = (
            f"{div_line1}\n"
            "SELECT\n"
            "    *\n"
            "FROM\n"
            f"    ({predict_query}\n) __PREDICT__\n"
            "JOIN\n"
            f"    ({expr_query}\n) __EXPR__\n"
            "ON\n"
            "    __PREDICT__.fk = __EXPR__.fk\n"
            "ORDER BY\n"
            "    __PREDICT__.fk ASC\n"
            f"{div_line2}"
        )

        return where_query

    def build_aggregation(self, aggr_dict: dict, ptable: str, ppk: str) -> str:
        r"""Builds a SQL query for a static PredQL aggregation.

        Just uses existing *build_stat_aggregation* method from base *`Converter`* class.

        Args:
            aggr_dict (dict): Parsed aggregation dictionary containing 'Table', 'Column', 'Where'(optional) keys.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            aggr_query (str): SQL query returning pairs (fk, comp_col).
        """
        aggr_query = self.build_stat_aggregation(aggr_dict, ptable, ppk)

        return aggr_query
