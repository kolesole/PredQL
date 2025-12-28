"""Static PredQL converter module for non-temporal queries."""

import textwrap

from relbench.base import Table

from predql.converter.converter import ConverterPredQL
from predql.converter.utils import get_div_line, get_indent


class SConverterPredQL(ConverterPredQL):
    r"""Static PredQL converter class for static conversion PredQL -> SQL.

    Converts static (non-temporal) PredQL queries into SQL queries.\
    Extends the base ConverterPredQL class with concrete implementations\
    for static prediction tasks.
    """

    def convert(self,
                predql_query : str,
                indent       : int=0) -> Table:
        r"""Converts the static PredQL query string into an executable SQL query.

        Returns the result as a *`Table`* object.

        Args:
            predql_query (str): The PredQL query string to be converted and executed.
            indent (int, optional): Indentation level for formatted SQL output, default is 0.

        Returns:
            out (Table): The *`Table`* object containing the result of the executed SQL query,\
                    with columns (*fk*, *label*) corresponding to the translated PredQL query output.
        """
        # parse PredQL query into dictionary
        query_dict = self.parse_query(predql_query)

        # check FOR EACH
        for_each_dict = query_dict["ForEach"]
        # extract parent table name
        ptable = for_each_dict["Table"]
        # extract primary key column name
        ppk = for_each_dict["Column"]

        # check if FOR_EACH has WHERE clause for filtering
        where_dict = for_each_dict["Where"]
        for_each_query = None
        # if exists -> build for_each_query
        # otherwise -> for_each_query remains None
        if where_dict:
            for_each_query = self.build_expr(where_dict["Expr"], ptable, ppk, indent)

        # build PREDICT query
        predict_dict = query_dict["Predict"]
        sql_query = self.build_predict(predict_dict, ptable, ppk, for_each_query, indent+1)

        # add semicolon to end of SQL query
        sql_query = f"{sql_query};"

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
                      for_each_query : str,
                      indent         : int=0) -> str:
        r"""Builds a SQL query for the PREDICT clause in static conversion.

        Args:
            query_dict (dict): Parsed dictionary of the PREDICT clause.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            for_each_query (str): SQL subquery from the FOR_EACH WHERE clause, providing base fk column, can be None.
            indent (int, optional): Indentation level for formatted SQL output, default is 0.

        Returns:
            predict_query (str): SQL subquery returning (fk, label) pairs.
        """
        # check predict type, build main_query and label_query accordingly
        # expr / id_dot_id
        pred_type = query_dict["PredType"]
        if pred_type == "expr":
            main_query = self.build_expr(query_dict["Expr"], ptable, ppk, indent+1)
            label_query = """
                CASE
                    WHEN main.fk IS NOT NULL THEN TRUE
                    ELSE FALSE
                END
                """

        elif pred_type == "id_dot_id":
            main_query = self.build_id_dot_id(query_dict, ptable, ppk, indent+1)
            label_query = "main.comp_col"
        else:
            raise ValueError(f"Unknown predict type: {pred_type}")

        # create division markers for formatted output
        div_line_pred1 = get_div_line("PREDICT_START")
        div_line_pred2 = get_div_line("PREDICT_END")

        # build final predict query depending on FOR EACH WHERE existence
        if for_each_query:
            predict_query = f"""
                {div_line_pred1}
                SELECT
                    for_each.fk AS fk,
                    {label_query} AS label
                FROM
                    ({for_each_query}) for_each
                LEFT JOIN
                    ({main_query}) main
                ON
                    main.fk = for_each.fk
                ORDER BY
                    main.fk ASC
                {div_line_pred2}
                """

        else:
            predict_query = f"""
                {div_line_pred1}
                SELECT
                    parent.{ppk} AS fk,
                    {label_query} AS label
                FROM
                    {ptable} parent
                LEFT JOIN
                    ({main_query}) main
                ON
                    main.fk = parent.{ppk}
                ORDER BY
                    parent.{ppk} ASC
                {div_line_pred2}
                """
        predict_query = textwrap.indent(predict_query, get_indent(indent))

        return predict_query


    def build_expr(self,
                   expr_dict : dict,
                   ptable    : str,
                   ppk       : str,
                   indent    : int=0) -> str:
        r"""Recursively builds a SQL query for a logical expression tree.

        Converts nested boolean expressions (from WHERE or ASSUMING clauses) into SQL.
        Combines sub-expressions using UNION (for OR) or INTERSECT (for AND) operations
        to return a set of foreign keys where the expression evaluates to true.

        Args:
            expr_dict (dict): Parsed dictionary of the expression (can contain 'Op',
                'Left', 'Right' keys or a single condition).
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.
            indent (int, optional): Indentation level for formatted SQL output, default is 0.

        Returns:
            expr_query (str): SQL query returning foreign keys where the expression is true.
        """
        # create division markers for formatted output
        div_line_expr1 = get_div_line("EXPR_START")
        div_line_expr2 = get_div_line("EXPR_END")

        # if expression is composite (AND/OR) -> recursively build left and right sub-expressions
        # otherwise -> build single condition expression
        if "Op" in expr_dict:
            # build left expession
            left_expr = self.build_expr(expr_dict["Left"], ptable, ppk, indent+1)
            # build right expression
            right_expr = self.build_expr(expr_dict["Right"], ptable, ppk, indent+1)

            # check operation and convert to SQL format for tables
            op = expr_dict["Op"].lower()
            if op == "and":
                filt = "INTERSECT"
            elif op == "or":
                filt = "UNION"
            else:
                raise ValueError(f"Unknown expression operator: {op}")

            expr_query = f"""
                {div_line_expr1}
                SELECT
                    fk,
                FROM
                    ({left_expr}) left_expr
                {filt}
                SELECT
                    fk,
                FROM ({right_expr}) right_expr
                {div_line_expr2}
                """
        else:
            expr_query = self.build_condition(expr_dict, ptable, ppk, indent+1)
        expr_query = textwrap.indent(expr_query, get_indent(indent))

        return expr_query

