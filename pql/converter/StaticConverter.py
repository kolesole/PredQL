from relbench.base import Table

from .Converter import PQLConverter

from .utils import build_aggr_func


class SPQLConverter(PQLConverter):
    def __init__(self, db, *args) -> None:
        super().__init__(db)
    
    
    def convert(self, pql_query : str):
        
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

        # assuming_dict = query_dict["Assuming"]
        # if assuming_dict:
        #     sql_query = self.build_assuming(assuming_dict, 
        #                                     ptable_name, 
        #                                     ppk_name,
        #                                     sql_query)

        where_dict = query_dict["Where"]
        where_query = None
        if where_dict:
            where_query = self.build_where(where_dict, 
                                           ptable_name, 
                                           ppk_name)
            
            sql_query = f"""
                            SELECT 
                                s.fk fk,
                                s.label
                            FROM 
                                ({sql_query}) s
                            JOIN
                                ({where_query}) w
                            ON
                                w.fk = s.fk
                            ORDER BY 
                                s.fk ASC
                             
                         """
        
        sql_query = f"{sql_query};"   

        print(sql_query)

        df = self.conn.sql(sql_query).df
        return Table(
            df=df,
            fkey_col_to_pkey_table=None,
            pkey_col=None,
            time_col=None,
            )
    

    # doesn't exist in STATIC query
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

        type_query = None
        label_query = None
        match pred_type:
            case "condition":
                type_query = self.build_condition(query_dict["Condition"], ptable_name, ppk_name)
                label_query = """CASE
                                     WHEN tq.fk IS NOT NULL THEN TRUE
                                     ELSE FALSE
                                 END
                              """
            case "id_dot_id":
                type_query = self.build_id_dot_id(query_dict, ptable_name, ppk_name)
                label_query = "tq.col_for_comp"
        
        predict_query = None
        if for_each_query:
            predict_query = f"""
                                SELECT
                                    fq.fk AS fk,
                                    {label_query} AS label
                                FROM
                                    ({for_each_query}) fq
                                LEFT JOIN
                                    ({type_query}) tq
                                ON
                                    tq.fk = fq.fk
                                ORDER BY 
                                    fq.fk ASC
                            """
        
        else:
            predict_query = f"""
                                SELECT
                                    p.{ppk_name} AS fk,
                                    {label_query} AS label
                                FROM
                                    {ptable_name} p
                                LEFT JOIN
                                    ({type_query}) tq
                                ON
                                    tq.fk = p.{ppk_name}
                                ORDER BY 
                                    p.{ppk_name} ASC
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
                             FROM
                                 ({left_query}) l
                             {filt}
                             SELECT
                                 fk AS fk,
                             FROM ({right_query}) r
                          """
        else:
            expr_query = self.build_condition(expr_dict, ptable_name, ppk_name)
        
        return expr_query


    # cant be in static PREDICT
    def build_aggregation(self, 
                          aggr_dict : dict,
                          ptable_name : str,  
                          ppk_name : str) -> str:
        table_name = aggr_dict["Table"]
        
        fk = self.find_fk(table_name, ptable_name, ppk_name)
        aggr_func = build_aggr_func(aggr_dict)

        res_query = f"""
                        SELECT 
                            tbl.{fk}           AS fk,
                            {aggr_func("tbl")} AS col_for_comp,
                        FROM
                            {table_name} tbl
                        GROUP BY tbl.{fk}"""

        # TODO
        # where_dict = aggr_dict["Where"]
        # if where_dict:
        #     where_query = self.build_where(where_dict, ptable_name, ppk_name)

        # TODO column_name can be "*" # DONE
        return res_query