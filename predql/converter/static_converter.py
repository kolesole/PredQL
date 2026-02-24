"""Static PredQL converter class for non-temporal queries."""

from predql.base import Database, Table
from predql.validator import SValidator

from predql.converter.converter import Converter
from predql.converter.utils import build_aggr_func, get_div_line


class SConverter(Converter):
    r"""Static PredQL converter class for static conversion PredQL -> SQL.

    Converts static (non-temporal) PredQL queries into SQL queries.  
    Extends the base Converter class with concrete implementations  
    for static prediction tasks.
    """

    def __init__(self,
                 db: Database) -> None:
        super().__init__(db)
        # initialize static validator
        self.validator = SValidator(self.collector, self.db)
        

    def convert(self,
                predql_query : str,
                show         : bool=False) -> Table:
        r"""Converts the static PredQL query string into an executable SQL query.

        Returns the result as a *`Table`* object.

        Args:
            predql_query (str): The PredQL query string to be converted and executed.
            show (bool): If True, prints the generated SQL query.

        Returns:
            out (Table): The *`Table`* object containing the result of the executed SQL query,  
                    with columns (*fk*, *label*) corresponding to the translated PredQL query output.
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
        
        # add semicolon to end of SQL query
        sql_query = f"{sql_query}\n;"

        if show:
            print(sql_query)

        # execute SQL query and return result as Table
        df = self.conn.sql(sql_query).df()
        return Table(
            df=df,
            fkey_col_to_pkey_table={"fk" : ptable}, # fk column in output table corresponds to pk of parent table
            pkey_col=None,
            time_col=None,
            )


    def build_for_each(self,
                       for_each_dict : dict) -> tuple[str, str, str]:
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
        ppk = for_each_dict["Column"].value

        # build static WHERE query if exists to filter parent table rows before prediction
        if where := for_each_dict["Where"]:
            for_each_query = self.build_stat_where(where.value, ptable, ppk)
            ptable = f"({for_each_query})"

        # build final FOR EACH query
        for_each_query = (
             "SELECT\n"
            f"    {ppk} AS fk\n"
             "FROM\n"
            f"    {ptable}\n"
        )

        return ptable_name, ppk, for_each_query


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
            for_each_query (str): SQL subquery from the FOR_EACH WHERE clause, providing base fk column.

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

        # build final PREDICT query
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
    

    def build_where(self,
                    where_dict    : dict,
                    ptable        : str,
                    ppk           : str,
                    predict_query : str) -> str:
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
        r"""Builds a SQL query for a static PredQL aggregation.

        Args:
            aggr_dict (dict): Parsed aggregation dictionary containing 'Table', 'Column', 'Where'(optional) keys.
            ptable (str): Name of the parent table.
            ppk (str): Name of the primary key column in the parent table.

        Returns:
            aggr_query (str): SQL query returning pairs (fk, comp_col).
        """
        # extract aggregation table
        aggr_table = aggr_dict["Table"].value

        # create division markers for formatted output
        div_line_aggr1 = get_div_line("AGGREGATION_START")
        div_line_aggr2 = get_div_line("AGGREGATION_END")

        # find foreign key column in the aggregation table that links to parent table
        fk = self.find_fk(aggr_table, ptable, ppk)
        
        # build SQL aggregation function with proper column references
        aggr_func = build_aggr_func(aggr_dict)
        aggr = aggr_func("aggr_tbl").replace("\n", "\n" + 4*" ") + "\n"

        # build static WHERE query if exists
        if where := aggr_dict["Where"]: 
            aggr_ppk = self.db.table_dict[aggr_table].pkey_col
            aggr_table = self.build_stat_where(where.value, aggr_table, aggr_ppk)
            aggr_table = f"({aggr_table})"

        # build aggregation query
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
