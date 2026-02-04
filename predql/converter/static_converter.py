"""Static PredQL converter module for non-temporal queries."""

from predql.base import Database, Table

from predql.converter.converter import Converter
from predql.converter.utils import get_div_line


class SConverter(Converter):
    r"""Static PredQL converter class for static conversion PredQL -> SQL.

    Converts static (non-temporal) PredQL queries into SQL queries.\
    Extends the base ConverterPredQL class with concrete implementations\
    for static prediction tasks.
    """

    def __init__(self,
                 db: Database) -> None:
        super().__init__(db)
        self.tmp = False
        
    def convert(self,
                predql_query : str) -> Table:
        r"""Converts the static PredQL query string into an executable SQL query.

        Returns the result as a *`Table`* object.

        Args:
            predql_query (str): The PredQL query string to be converted and executed.

        Returns:
            out (Table): The *`Table`* object containing the result of the executed SQL query,\
                    with columns (*fk*, *label*) corresponding to the translated PredQL query output.
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

        # add semicolon to end of SQL query
        sql_query = f"{sql_query}\n;"

        print(sql_query)

        # execute SQL query and return result as Table
        df = self.conn.sql(sql_query).df
        return Table(
            df=df,
            fkey_col_to_pkey_table=None,
            pkey_col=None,
            time_col=None,
            )


    def build_predict(self,
                      query_dict     : dict,
                      ptable         : str,
                      ppk            : str,
                      for_each_query : str) -> str:
        r"""Builds a SQL query for the PREDICT clause in static conversion.

        Args:
            query_dict (dict): Parsed dictionary of the PREDICT clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            for_each_query (str): SQL subquery from the FOR_EACH WHERE clause, providing base fk column, can be None.

        Returns:
            predict_query (str): SQL subquery returning (fk, label) pairs.
        """
        # check predict type, build main_query and label_query accordingly
        # expr / id_dot_id
        pred_type = query_dict["PredType"]
        if pred_type == "expr":
            main_query = self.build_expr(query_dict["Expr"].value, ptable, ppk)
            label_query = (
                "CASE\n"
                "    WHEN main.fk IS NOT NULL THEN TRUE\n"
                "    ELSE FALSE\n"
                "END"
            )
        elif pred_type == "id_dot_id":
            main_query = self.build_id_dot_id(query_dict, ptable, ppk)
            label_query = "main.comp_col"
        else:
            raise ValueError(f"Unknown predict type: {pred_type}")
        main_query = main_query.replace("\n", "\n" + 4*" ") + "\n"
        label_query = label_query.replace("\n", "\n" + 4*" ") + "\n"

        # create division markers for formatted output
        div_line_pred1 = get_div_line("PREDICT_START")
        div_line_pred2 = get_div_line("PREDICT_END")

        # build final predict query depending on FOR EACH WHERE existence
        if for_each_query:
            for_each_query = for_each_query.replace("\n", "\n" + 4*" ") + "\n"
            predict_query = (
                f"{div_line_pred1}\n"
                 "SELECT\n"
                 "    for_each.fk AS fk,\n"
                f"    {label_query} AS label\n"
                 "FROM\n"
                f"    ({for_each_query}) for_each\n"
                 "LEFT JOIN\n"
                f"    ({main_query}) main\n"
                 "ON\n"
                 "    main.fk = for_each.fk\n"
                 "ORDER BY\n"
                 "    main.fk ASC\n"
                f"{div_line_pred2}"
            )
        else:
            predict_query = (
                f"{div_line_pred1}\n"
                 "SELECT\n"
                f"    parent.{ppk} AS fk,\n"
                f"    {label_query} AS label\n"
                 "FROM\n"
                f"    {ptable} parent\n"
                 "LEFT JOIN\n"
                f"    ({main_query}) main\n"
                 "ON\n"
                f"    main.fk = parent.{ppk}\n"
                 "ORDER BY\n"
                f"    parent.{ppk} ASC\n"
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
        to return a set of foreign keys where the expression evaluates to true.

        Args:
            expr_dict (dict): Parsed dictionary of the expression (can contain 'Op',
                'Left', 'Right' keys or a single condition).
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            expr_query (str): SQL query returning foreign keys where the expression is true.
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
                raise ValueError(f"Unknown expression operator: {op}")

            expr_query = (
                f"{div_line_expr1}\n"
                 "SELECT\n"
                 "    fk,\n"
                 "FROM\n"
                f"    ({left_expr}) left_expr\n"
                f"{filt}\n"
                 "SELECT\n"
                 "    fk,\n"
                f"FROM ({right_expr}) right_expr\n"
                f"{div_line_expr2}"
            )
        else:
            expr_query = self.build_condition(expr_dict.value, ptable, ppk)

        return expr_query
