import pandas as pd

from relbench.base import Database, Table

from .Converter import PQLConverter
from .utils import build_aggr_func


class TPQLConverter(PQLConverter):
    def __init__(self, 
                 db : Database, 
                 timestamps : "pd.Series[pd.Timestamp]"):
        r"""
        Create a PQLConverter object.

        The function performs the following steps:
            - stores a reference to the provided Database object;
            - create a PQLVisitor instance for query traversal;
            - opens a temporary DuckDB connection and registers all tables from db;
            - if timestamps ...;
            - regiters timestamps_df table with one column - timestamp.

        Args
        ----
            db : Database
                Database object containing the tables.
            timestamp : pd.Series[pd.Timestamp], optional
                Initial time points for predictions
                If not provided.
        """

        super().__init__(db)
                
        self.timestamps = timestamps
        timestamp_df = pd.DataFrame({"timestamp" : self.timestamps})
        self.conn.register("timestamp_df", timestamp_df)
        self.time_col = "timestamp"
    

    def convert(self, pql_query : str):
        r"""
        Convert a PQL query string into an executable SQL query and return the result as a Table object.

        The function acts as the main entry point for translating PQL into SQL. 
        It first parses the query, identifies its structural components, constructs
        the corresponding SQL subqueries, executes the final SQL query using DuckDB, 
        and returns the result as a Table instance.

        The function performs the following steps:
            - parses the given PQL query string into a dictionary using parse_query;
            - extracts the for_each clause to determine the base table and primary key;
            - builds conditional subqueries for where, assuming, and predict parts;
            - combines these parts into a final SQL query;
            - executes the SQL query using DuckDB;
            - wraps the resulting DataFrame in a Table object.

        Args
        ----
            `pql_query` : str
                The PQL query string to be converted and executed.

        Returns
        -------
            Table
                A Table object containing the result of the executed SQL query, 
                with columns corresponding to the translated PQL query output.
        """
        
        query_dict = self.parse_query(pql_query)

        for_each_dict = query_dict["ForEach"]
        ptable_name = for_each_dict["Table"]
        ppk_name = for_each_dict["Column"]
        for_each_query = None
        if for_each_dict["Where"]:
            for_each_query = self.build_where(for_each_dict["Where"], 
                                              ptable_name, 
                                              ppk_name)
        
        predict_dict = query_dict["Predict"]
        sql_query = self.build_predict(predict_dict, 
                                       ptable_name, 
                                       ppk_name,
                                       for_each_query)

        assuming_dict = query_dict["Assuming"]
        if assuming_dict:
            sql_query = self.build_assuming(assuming_dict, 
                                            ptable_name, 
                                            ppk_name,
                                            sql_query)

        where_dict = query_dict["Where"]
        where_query = None
        if where_dict:
            where_query = self.build_where(where_dict, 
                                           ptable_name, 
                                           ppk_name)
            
            sql_query = f"""
                            SELECT 
                                s.fk fk,
                                s.timestamp,
                                s.label
                            FROM 
                                ({sql_query}) s
                            JOIN
                                ({where_query}) w
                            ON
                                w.fk = s.fk
                            AND
                                w.timestamp = s.timestamp
                            ORDER BY 
                                s.timestamp ASC, s.fk ASC
                             
                         """
        
        sql_query = f"{sql_query};"   

        print(sql_query)

        df = self.conn.sql(sql_query).df
        return Table(
            df=df,
            fkey_col_to_pkey_table=None,
            pkey_col=None,
            time_col="timestamp",
            )
    

    def build_assuming(self, 
                       query_dict : dict,
                       ptable_name : str, 
                       ppk_name : str,
                       predict_query : str) -> str:
        expr_dict = query_dict["Expr"]
        expr_query = self.build_expr(expr_dict, ptable_name, ppk_name)

        help_query = f"""
                         SELECT 
                             p.{ppk_name} AS {ppk_name},
                             pred.timestamp  AS timestamp,
                             pred.label AS label
                         FROM 
                             {ptable_name} p
                         JOIN
                             ({predict_query}) pred
                         ON
                             pred.fk = p.{ppk_name}
                      """
            
        assuming_query = f"""
                             SELECT
                                 hq.{ppk_name} AS {ppk_name},
                                 hq.timestamp  AS timestamp
                             FROM
                                 ({help_query}) hq
                             JOIN
                                 ({expr_query}) eq
                             ON
                                 eq.fk = hq.{ppk_name}
                             AND
                                 eq.timestamp = hq.timestamp
                             ORDER BY 
                                 hq.timestamp ASC, hq.{ppk_name} ASC
                          """
        
        return assuming_query


    def build_predict(self, 
                      query_dict : dict,
                      ptable_name : str,  
                      ppk_name : str,
                      for_each_query : str) -> str:
        pred_type = query_dict["PredType"]

        type_query = None # aggr and id_dot_id are not supported yet
        label_query = None
        match pred_type:
            case "aggregation":
                type_query = self.build_aggregation(query_dict["Aggregation"], ptable_name, ppk_name)
                label_query = "tq.col_for_comp"
            case "condition":
                type_query = self.build_condition(query_dict["Condition"], ptable_name, ppk_name)
                label_query = """CASE
                                     WHEN tq.fk IS NOT NULL THEN TRUE
                                     ELSE FALSE
                                 END
                              """
            case "id_dot_id": # STATIC TASK
                table_query = self.build_id_dot_id(query_dict, ptable_name, ppk_name)
        
        predict_query = None
        if for_each_query:
            help_query = f"""
                             SELECT 
                                 p.{ppk_name} AS {ppk_name},
                                 c.timestamp  AS timestamp,
                             FROM 
                                 {ptable_name} p
                             JOIN
                                 ({for_each_query}) c
                             ON
                                 c.fk = p.{ppk_name}
                        """
            
            predict_query = f"""
                                SELECT
                                    hq.{ppk_name} AS fk,
                                    hq.timestamp  AS timestamp,
                                    {label_query} AS label
                                FROM
                                    ({help_query}) hq
                                LEFT JOIN
                                    ({type_query}) tq
                                ON
                                    tq.fk = hq.{ppk_name}
                                AND
                                    tq.timestamp = hq.timestamp
                                ORDER BY 
                                    hq.timestamp ASC, hq.{ppk_name} ASC
                            """
        
        else:
            predict_query = f"""
                                SELECT
                                    p.{ppk_name} AS fk,
                                    time.timestamp AS timestamp,
                                    {label_query} AS label
                                FROM
                                    {ptable_name} p
                                CROSS JOIN  
                                    timestamp_df time
                                LEFT JOIN
                                    ({type_query}) tq
                                ON
                                    tq.fk = p.{ppk_name}
                                    AND
                                    tq.timestamp = time.timestamp
                                ORDER BY 
                                    time.timestamp ASC, p.{ppk_name} ASC
                            """       

        return predict_query
    

    def build_where(self, 
                    query_dict : dict,
                    ptable_name : str,  
                    ppk_name : str) -> str:
        expr_dict = query_dict["Expr"]
        expr_query = self.build_expr(expr_dict, ptable_name, ppk_name)
        return expr_query

    
    def build_expr(self, 
                   expr_dict : dict,
                   ptable_name : str,
                   ppk_name : str) -> str:
        
        expr_query = None
        if "Op" in expr_dict:
            left_query = self.build_expr(expr_dict["Left"], ptable_name, ppk_name)
            right_query = self.build_expr(expr_dict["Right"], ptable_name, ppk_name)

            op = expr_dict["Op"].lower()
            filt = None
            if op == "and":
                filt = "INTERSECT"
            elif op == "or":
                filt = "UNION"
            else:
                pass
            expr_query = f"""
                             SELECT 
                                 fk AS fk, 
                                 timestamp AS timestamp
                             FROM
                                 ({left_query}) l
                             {filt}
                             SELECT
                                 fk AS fk,
                                 timestamp AS timestamp
                             FROM ({right_query}) r
                          """
        else:
            expr_query = self.build_condition(expr_dict, ptable_name, ppk_name)
        
        return expr_query


    def build_aggregation(self, 
                          aggr_dict : dict,
                          ptable_name : str,  
                          ppk_name : str) -> str:
        table_name = aggr_dict["Table"]
        start = int(aggr_dict["Start"])
        end = int(aggr_dict["End"])
        measure_unit = aggr_dict["MeasureUnit"].upper().removesuffix("S")
        
        fk = self.find_fk(table_name, ptable_name, ppk_name)
        time_column = self.find_time_column(table_name)
        aggr_func = build_aggr_func(aggr_dict)

        res_query = f"""
                        SELECT 
                            tbl.{fk}           AS fk,
                            {aggr_func("tbl")} AS col_for_comp,
                            time.timestamp     AS timestamp
                        FROM
                            timestamp_df time
                        JOIN
                            {table_name} tbl
                        ON 
                            tbl.{time_column} >= time.timestamp + INTERVAL '{start} {measure_unit}'
                            AND
                            tbl.{time_column} < time.timestamp + INTERVAL '{end} {measure_unit}'
                        GROUP BY time.timestamp, tbl.{fk}"""

        where_dict = aggr_dict["Where"]
        if where_dict:
            where_query = self.build_where(where_dict, ptable_name, ppk_name)
            res_query = f"""
                            SELECT
                                rq.fk              AS fk,
                                rq.col_for_comp    AS col_for_comp,
                                rq.timestamp       AS timestamp
                            FROM 
                                {res_query} rq
                            JOIN
                                {where_query} wq
                            ON 
                                wq.fk = rq.fk
                            AND
                                wq.timestamp = rq.timestamp
                            """

        return res_query
    

    def find_time_column(self,
                         table_name : str) -> str:
        r"""
        Find the name of the time column for a given table.

        The function looks up the specified table in the database dictionary
        and returns the name of its associated time column.

        Args
        ----
            `table_name` : str
                Name of the table whose time column is to be found.

        Returns
        -------
            str
                The name of the time column associated with the specified table.
        """

        table = self.db.table_dict[table_name]

        return table.time_col
        
