import pandas as pd

import textwrap

from relbench.base import Database, Table

from pql.converter.converter import ConverterPQL

from pql.converter.utils import build_aggr_func, get_div_line, get_indent


class TConverterPQL(ConverterPQL):
    r"""
    Temporal PQL converter class for temporal conversion PQL -> SQL.
    
    Converts temporal (time-series) PQL queries into SQL queries.\
    Extends the base ConverterPQL class with concrete implementations\
    for temporal prediction tasks with time window support.
    """

    def __init__(self, 
                 db         : Database, 
                 timestamps : "pd.Series[pd.Timestamp]") -> None:
        r"""
        Initializes a temporal PQL converter with timestamp support.

        Args:
            `db` (`Database`): Database object containing the tables.
            `timestamps` (`pd.Series[pd.Timestamp]`): Initial time points for predictions.
        
        Returns:
            `out` (`None`):
        """

        super().__init__(db)
        
        # store timestamps for temporal prediction
        self.timestamps = timestamps
        # create DataFrame with timestamp column for temporal operations
        timestamp_df = pd.DataFrame({"timestamp" : self.timestamps})
        # register timestamp_df in DuckDB for SQL queries
        self.conn.register("timestamp_df", timestamp_df)
    

    def convert(self, 
                pql_query : str,
                indent    : int=0) -> Table:
        r"""
        Converts the temporal PQL query string into an executable SQL query\ 
        and returns the result as a *`Table`* object.

        Args:
            `pql_query` (`str`): The PQL query string to be converted and executed.
            `indent` (`int`, optional): Indentation level for formatted SQL output, default is 0.

        Returns:
            `out` (`Table`): The *`Table`* object containing the result of the executed SQL query,\
                    with columns (*fk*, *timestamp*, *label*) corresponding to the translated PQL query output.
        """
        
        # parse PQL query into dictionary
        query_dict = self.parse_query(pql_query)
        
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

        # check ASSUMING clause to filter predictions
        assuming_dict = query_dict["Assuming"]
        if assuming_dict:
            sql_query = self.build_assuming(assuming_dict, ptable, ppk, sql_query, indent+1)

        # handle WHERE conditions from PREDICT clause
        # NOTE: will be moved to build_predict in future versions(for nested WHERE in aggregation)
        predict_aggr_dict = predict_dict["Aggregation"]
        if predict_aggr_dict:
            predict_where_dict = predict_aggr_dict["Where"]
            # if WHERE exists in aggregation -> apply additional filtering
            if predict_where_dict:
                help_query = self.build_expr(predict_where_dict["Expr"], ptable, ppk)

                sql_query = f"""
                    SELECT 
                        sq.fk,
                        sq.timestamp,
                        sq.label
                    FROM 
                        ({sql_query}) sq
                    JOIN 
                        ({help_query}) hq
                    ON 
                        hq.fk = sq.fk
                    ORDER BY 
                        sq.timestamp ASC, sq.fk ASC
                            """
        
        # add semicolon to end of SQL query
        sql_query = f"{sql_query};"   

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
                       predict_query : str,
                       indent        : int=0) -> str:
        r"""
        Restricts a temporal prediction query using an ASSUMING expression.

        Filters prediction results to keep only rows where the ASSUMING condition is true.
        Works by joining the prediction results with the ASSUMING expression on both fk and timestamp,
        preserving the label column only for matching rows.

        Args:
            `query_dict` (`dict`): Parsed dictionary of the ASSUMING clause.
            `ptable` (`str`): Name of the parent table.
            `ppk` (str): Name of the primary key column in the parent table.
            `predict_query` (str): The SQL subquery for the PREDICT part (fk, timestamp, label).
            `indent` (int, optional): Indentation level for formatted SQL output, default is 0.

        Returns:
            `assuming_query` (`str`): The SQL query filtering predictions using ASSUMING with temporal constraints.
        """
        
        # build assuming expression
        expr_dict = query_dict["Expr"]
        expr_query = self.build_expr(expr_dict, ptable, ppk)

        # create division markers for formatted output
        div_line_ass1 = get_div_line("ASSUMING_START")
        div_line_ass2 = get_div_line("ASSUMING_END")
        div_line_help1 = get_div_line("HELP_PART_START")
        div_line_help2 = get_div_line("HELP_PART_END")
            
        # build ASSUMING query with temporal join
        assuming_query = f"""
            {div_line_ass1}
            SELECT
                help.{ppk},
                help.timestamp
            FROM
                (
            {div_line_help1}
                SELECT 
                    parent.{ppk},
                    predict.timestamp,
                    predict.label
                FROM 
                    {ptable} parent
                JOIN
                    ({predict_query}) predict
                ON
                    predict.fk = parent.{ppk}
            {div_line_help2}
                ) help
            JOIN
                ({expr_query}) expr
            ON
                expr.fk = help.{ppk}
            AND
                expr.timestamp = help.timestamp
            ORDER BY 
                help.timestamp ASC, help.{ppk} ASC
            {div_line_ass2}
            """
        assuming_query = textwrap.indent(assuming_query, get_indent(indent))
        
        return assuming_query


    def build_predict(self, 
                      query_dict     : dict,
                      ptable         : str,  
                      ppk            : str,
                      for_each_query : str,
                      indent         : int=0) -> str:
        r"""
        Builds the SQL query for the PREDICT clause in temporal conversion.

        Handles temporal prediction logic by cross-joining with prediction timestamps and
        implementing different label generation strategies based on prediction type.

        Args:
            `query_dict` (`dict`): Parsed dictionary of the PREDICT clause.
            `ptable` (`str`): Name of the parent table.
            `ppk` (`str`): Name of the primary key column in the parent table.
            `for_each_query` (`str`): SQL subquery from FOR_EACH WHERE (can be None).
            `indent` (`int`, optional): Indentation level for formatted SQL output, default is 0.

        Returns:
            `predict_query` (`str`): SQL subquery returning (fk, timestamp, label) triples.
        """
        
        # check predict type, build main_query and label_query accordingly
        # aggregation / expr
        pred_type = query_dict["PredType"]
        if pred_type == "aggregation":
            main_query = self.build_aggregation(query_dict["Aggregation"], ptable, ppk, indent+1)
            
            # determine label extraction logic based on modifiers
            if query_dict["Classify"]:
                # CLASSIFY: use aggregated value directly
                label_query = "main.comp_col"
            elif query_dict["RankTop"]:
                # RANK_TOP K: keep only top K elements from aggregation
                K = int(query_dict["K"])
                label_query = f"""
                    CASE 
                        WHEN ARRAY_LENGTH(main.comp_col) > {K} THEN main.comp_col[1:{K}]
                        ELSE main.comp_col
                    END
                    """
            else:
                # default: use full aggregated value
                label_query = "main.comp_col"
        elif pred_type == "expr":
            main_query = self.build_expr(query_dict["Expr"], ptable, ppk, indent+1)

            label_query = """
                CASE
                    WHEN main.fk IS NOT NULL THEN TRUE
                    ELSE FALSE
                END
                """
        else:
            raise ValueError(f"Unknown predict type: {pred_type}")

        # create division markers for formatted output
        div_line_pred1 = get_div_line("PREDICT_START")
        div_line_pred2 = get_div_line("PREDICT_END")
        div_line_help1 = get_div_line("HELP_PART_START")
        div_line_help2 = get_div_line("HELP_PART_END")
        
        # build final predict query depending on FOR EACH WHERE existence
        if for_each_query:
            predict_query = f"""
                {div_line_pred1}
                SELECT
                    help.{ppk} AS fk,
                    help.timestamp  AS timestamp,
                    {label_query} AS label
                FROM
                    (
                {div_line_help1}
                    SELECT 
                        parent.{ppk},
                        for_each.timestamp,
                    FROM 
                        {ptable} parent
                    JOIN
                        ({for_each_query}) for_each
                    ON
                        for_each.fk = parent.{ppk}
                {div_line_help2}
                    ) help
                LEFT JOIN
                    ({main_query}) main
                ON
                    main.fk = help.{ppk}
                AND
                    main.timestamp = help.timestamp
                ORDER BY 
                    help.timestamp ASC, help.{ppk} ASC
                {div_line_pred2}
                """
        
        else:
            predict_query = f"""
                {div_line_pred1}
                SELECT
                    parent.{ppk} AS fk,
                    time.timestamp AS timestamp,
                    {label_query} AS label
                FROM
                    {ptable} parent
                CROSS JOIN  
                    timestamp_df time
                LEFT JOIN
                    ({main_query}) main
                ON
                    main.fk = parent.{ppk}
                AND
                    main.timestamp = time.timestamp
                ORDER BY 
                    time.timestamp ASC, parent.{ppk} ASC
                {div_line_pred2}
                """
        predict_query = textwrap.indent(predict_query, get_indent(indent))       

        return predict_query
    
    
    def build_expr(self, 
                   expr_dict : dict,
                   ptable    : str,
                   ppk       : str,
                   indent    : int=0) -> str:
        r"""
        Recursively builds a SQL query for a logical expression tree.

        Converts nested boolean expressions (from WHERE or ASSUMING clauses) into SQL.
        Combines sub-expressions using UNION (for OR) or INTERSECT (for AND) operations
        to return a set of (foreign key, timestamp) pairs where the expression evaluates to true.

        Args:
            `expr_dict` (`dict`): Parsed dictionary of the expression (can contain 'Op', 'Left', 'Right' keys or a single condition).
            `ptable` (`str`): Name of the parent table.
            `ppk` (`str`): Name of the primary key column in the parent table.
            `indent` (`int`, optional): Indentation level for formatted SQL output, default is 0.

        Returns:
            `expr_query` (`str`): SQL query returning (foreign key, timestamps pairs) where the expression is true.
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
                raise ValueError(f"Unknown operation in expression: {op}")

            expr_query = f"""
                {div_line_expr1}
                SELECT 
                    fk, 
                    timestamp
                FROM
                    ({left_expr}) left_expr
                {filt}
                SELECT
                    fk,
                    timestamp
                FROM 
                    ({right_expr}) right_expr
                {div_line_expr2}
                """

        else:
            expr_query = self.build_condition(expr_dict, ptable, ppk, indent+1)
        expr_query = textwrap.indent(expr_query, get_indent(indent))
        
        return expr_query


    def build_aggregation(self, 
                          aggr_dict : dict,
                          ptable    : str,  
                          ppk       : str,
                          indent    : int=0) -> str:
        r"""
        Builds the SQL query for a PQL aggregation over a time window.

        Computes aggregations relative to prediction timestamps within a defined
        `[start, end)` time window.

        Args:
            `aggr_dict` (`dict`): Parsed aggregation dictionary with Table, Start, End, MeasureUnit.
            `ptable` (`str`): Name of the parent table.
            `ppk` (`str`): Name of the primary key column in the parent table.
            `indent` (`int`, optional): Indentation level for formatted SQL output, default is 0.

        Returns:
            `aggr_query` (`str`): SQL query returning (fk, col_for_comp, timestamp) where col_for_comp is aggregated.
        """
        
        # extract aggregation parameters
        table = aggr_dict["Table"]
        start = int(aggr_dict["Start"])
        end = int(aggr_dict["End"])
        # remove trailing 'S' from measure unit for SQL syntax
        measure_unit = aggr_dict["MeasureUnit"].upper().removesuffix("S")

        # create division markers for formatted output
        div_line_aggr1 = get_div_line("AGGREGATION_START")
        div_line_aggr2 = get_div_line("AGGREGATION_END")

        # find foreign key column in the aggregation table that links to parent table
        fk = self.find_fk(table, ptable, ppk)
        # find time column for temporal filtering
        time_column = self.find_time_column(table)
        # build SQL aggregation function with proper column references
        aggr_func = build_aggr_func(aggr_dict, fk, time_column, ppk)

        # build temporal aggregation query
        aggr_query = f"""
            {div_line_aggr1}
            SELECT 
                parent.{ppk} AS fk,
                {aggr_func("aggr_tbl")} AS comp_col,
                time.timestamp AS timestamp
            FROM
                {ptable} parent
            CROSS JOIN
                timestamp_df time
            LEFT JOIN
                {table} aggr_tbl
            ON 
                aggr_tbl.{fk} = parent.{ppk}
            AND
                aggr_tbl.{time_column} >= time.timestamp + INTERVAL '{start} {measure_unit}'
            AND
                aggr_tbl.{time_column} < time.timestamp + INTERVAL '{end} {measure_unit}'
            GROUP BY 
                time.timestamp, parent.{ppk}
            {div_line_aggr2}
            """
        aggr_query = textwrap.indent(aggr_query, get_indent(indent))

        return aggr_query


    def find_time_column(self,
                         table_name : str) -> str:
        r"""
        Finds the name of the time column for a given table.

        Args:
            `table_name` (`str`): Name of the table whose time column is to be found.

        Returns:
            `out` (`str`): The name of the time column associated with the specified table.
        """
        
        table = self.db.table_dict[table_name]

        return table.time_col
    

        
