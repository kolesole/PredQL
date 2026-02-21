"""Static PredQL converter module for non-temporal queries."""

from predql.base import Database, Table
from predql.validator import SValidator

from predql.converter.converter import Converter
from predql.converter.utils import build_aggr_func, get_div_line


class SConverter(Converter):
    r"""Static PredQL converter class for static conversion PredQL -> SQL.

    Converts static (non-temporal) PredQL queries into SQL queries.\
    Extends the base ConverterPredQL class with concrete implementations\
    for static prediction tasks.
    """

    def __init__(self,
                 db: Database) -> None:
        super().__init__(db)
        self.validator = SValidator(self.collector, self.db)
        
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
        query_dict = query_dict["QueryStat"].value

        # check FOR EACH
        for_each_dict = query_dict["ForEach"].value
        ptable, ppk, for_each_query = self.build_for_each(for_each_dict)

        # build PREDICT query
        predict_dict = query_dict["Predict"].value
        sql_query = self.build_predict(predict_dict, ptable, ppk, for_each_query)

        if where := query_dict["Where"]:
            where_dict = where.value
            sql_query = self.build_where(where_dict, ptable, ppk, sql_query)
        
        # add semicolon to end of SQL query
        sql_query = f"{sql_query}\n;"

        print(sql_query)

        # execute SQL query and return result as Table
        df = self.conn.sql(sql_query).df
        return Table(
            df=df,
            fkey_col_to_pkey_table={"fk" : ptable},
            pkey_col=None,
            time_col=None,
            )


    def build_for_each(self,
                       for_each_dict : dict) -> list[str, str, str]:
        ptable = for_each_dict["Table"].value
        ppk = for_each_dict["Column"].value

        if where := for_each_dict["Where"]:
            for_each_query = self.build_stat_where(where.value, ptable, ppk)
            ptable = f"({ptable})"

        for_each_query = (
             "SELECT\n"
            f"    {ppk} AS fk\n"
             "FROM\n"
            f"    {ptable}\n"
        )

        return ptable, ppk, for_each_query


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
            pass

        main_query = main_query.replace("\n", "\n" + 4*" ") + "\n"
        label_query = label_query.replace("\n", "\n" + 4*" ") + "\n"

        # create division markers for formatted output
        div_line_pred1 = get_div_line("PREDICT_START")
        div_line_pred2 = get_div_line("PREDICT_END")

        # build final predict query depending on FOR EACH WHERE existence
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
             "    for_each.fk ASC\n"
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
        expr_query = self.build_stat_expr(expr_dict, ptable, ppk)
        return expr_query
    


    
        # create division markers for formatted output
        div_line_expr1 = get_div_line("EXPR_START")
        div_line_expr2 = get_div_line("EXPR_END")

        # if expression is composite (AND/OR) -> recursively build left and right sub-expressions
        # otherwise -> build single condition expression
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            # build left expession
            left_expr = self.build_expr(expr_dict["LeftExpr"], ptable, ppk)
            left_expr = left_expr.replace("\n", "\n" + 4*" ") + "\n"
            # build right expression
            right_expr = self.build_expr(expr_dict["RightExpr"], ptable, ppk)
            right_expr = right_expr.replace("\n", "\n" + 4*" ") + "\n"

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
    

    def build_where(self,
                    where_dict    : dict,
                    ptable        : str,
                    ppk           : str,
                    predict_query : str) -> str:
        expr_query = self.build_expr(where_dict["Expr"].value, ptable, ppk)
        where_query = (
             "SELECT\n"
             "    *\n"
             "FROM\n"
            f"    ({predict_query}\n) predict\n"
             "JOIN\n"
            f"    ({expr_query}\n) expr\n"
             "ON\n"
             "    predict.fk = expr.fk\n"
             "ORDER BY\n"
             "    predict.fk ASC\n"
        )

        return where_query
    

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
        aggr_table = aggr_dict["Table"].value

        # create division markers for formatted output
        div_line_aggr1 = get_div_line("AGGREGATION_START")
        div_line_aggr2 = get_div_line("AGGREGATION_END")

        # find foreign key column in the aggregation table that links to parent table
        fk = self.find_fk(aggr_table, ptable, ppk)
        # find time column for temporal filtering
        # build SQL aggregation function with proper column references
        aggr_func = build_aggr_func(aggr_dict)
        aggr = aggr_func("aggr_tbl").replace("\n", "\n" + 4*" ") + "\n"

        if where := aggr_dict["Where"]: 
            aggr_ppk = self.db.table_dict[aggr_table].pkey_col
            aggr_table = self.build_stat_where(where.value, aggr_table, aggr_ppk)
            aggr_table = f"({aggr_table})"

        # build static aggregation query
        aggr_query = (
            f"{div_line_aggr1}\n"
             "SELECT\n"
            f"    parent.{ppk} AS fk,\n"
            f"    {aggr} AS comp_col,\n"
             "FROM\n"
            f"    {ptable} parent\n"
             "LEFT JOIN\n"
            f"    {aggr_table} aggr_tbl\n"
             "ON\n"   
            f"    aggr_tbl.{fk} = parent.{ppk}\n"
             "GROUP BY\n"
            f"    time.timestamp, parent.{ppk}\n"
            f"{div_line_aggr2}" 
        )

        return aggr_query

        

