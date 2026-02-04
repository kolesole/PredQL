from abc import abstractmethod
from enum import Enum, auto

from predql.base import Database, Table
from predql.validator import Error, ErrorCollector
from predql.visitor import ParsedValue


AGGR_NUM_COND = ["avg", "count", "count_disitnct", "first", "last", "max", "min", "sum"]
AGGR_STR_COND = ["first", "last"]
AGGR_NULL_COND = AGGR_NUM_COND + ["list_disitnct"]


class Context(Enum):
    FROM_PREDICT = auto()
    FROM_WHERE = auto()
    FROM_ASSUMING = auto()


class Validator:
    
    def __init__(self,
                 collector : ErrorCollector, 
                 db        : Database,
                 tmp       : bool) -> None:
        self.collector = collector
        self.db = db
        self.tmp = tmp


    def validate_query_dict(self, 
                            query_dict : dict) -> None:
        if query_dict is None:
            return
        
        ptable_name = self.validate_for_each_dict(query_dict["ForEach"])
        self.validate_predict_dict(query_dict["Predict"], ptable_name)
        self.validate_assuming_dict(query_dict["Assuming"], ptable_name)
        self.validate_where_dict(query_dict["Where"], ptable_name)


    def validate_for_each_dict(self, 
                               for_each : ParsedValue) -> str:
        if for_each is None:
            return
        
        for_each_dict = for_each.value

        table_token = for_each_dict["Table"]
        table_name = table_token.value
        if not self.is_table_in_db(table_name):
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"Table '{table_name}' in FOR EACH clause does not exist in database.")

        column_token = for_each_dict["Column"]
        column_name = column_token.value
        if not self.is_column_in_table(table_name, column_name):
            self.collector.val_error(line=column_token.line,
                                     column=column_token.column,
                                     msg=f"Column '{column_name}' in FOR EACH clause does not exist in table '{table_name}'.")
            
        if not self.is_pkey_col(table_name, column_name):
            self.collector.val_error(line=column_token.line,
                                     column=column_token.column,
                                     msg=f"Column '{column_name}' in FOR EACH clause must be a primary key column of table '{table_name}'.")
        
        # if where := for_each_dict["Where"]:
        #     self.collector.val_error(line=where.line,
        #                              column=where.column,
        #                              msg="WHERE clause in FOR EACH clause is not yet supported.")
        self.validate_where_dict(for_each_dict["Where"], table_name)

        return table_token.value


    def validate_predict_dict(self, 
                              predict : ParsedValue,
                              ptable_name  : str) -> None:
        if predict is None:
            return
        
        predict_dict = predict.value
        match predict_dict["PredType"]:
            case "aggregation":
                aggr = predict_dict["Aggregation"]
                self.validate_aggr_dict(aggr, ptable_name, Context.FROM_PREDICT)
                aggr_dict = aggr.value
                aggr_type = aggr_dict["AggrType"].value
                
                if aggr_type.lower() != "list_distinct":
                    if classify_token := predict_dict["Classify"]:
                        self.collector.val_error(line=classify_token.line,
                                                 column=classify_token.column,
                                                 msg=f"CLASSIFY modifier is only allowed with LIST_DISTINCT aggregation, found with {aggr_type}.")
                    
                    if rank_top_token := predict_dict["RankTop"]:
                        self.collector.val_error(line=rank_top_token.line,
                                                 column=rank_top_token.column,
                                                 msg=f"RANK_TOP K modifier is only allowed with LIST_DISTINCT aggregation, found with {aggr_type}.")

                if K_token := predict_dict["K"]:
                    K = K_token.value
                    if K <= 0:
                        self.collector.val_error(line=K_token.line,
                                                 column=K_token.column,
                                                 msg=f"K in RANK_TOP K must be a positive integer, found {K}.")
            case "expr":
                self.validate_expr_dict(predict_dict["Expr"], ptable_name, Context.FROM_PREDICT)
            case "id_dot_id":
                if self.tmp:
                    self.collector.val_error(line=predict.line,
                                             column=predict.column,
                                             msg="Use SConverter for static predictions.")
                
                table_token = predict_dict["Table"]
                table_name = table_token.value
                if not self.is_table_in_db(table_name):
                    self.collector.val_error(line=table_token.line,
                                             column=table_token.column,
                                             msg=f"Table '{table_name}' in PREDICT clause does not exist in database.")

                if not self.has_conn_with_main_table(table_name, ptable_name):
                    self.collector.val_error(line=table_token.line,
                                             column=table_token.column,
                                             msg=f"Table '{table_name}' in PREDICT clause must have a connection with main table '{ptable_name}'.")
                
                column_token = predict_dict["Column"]
                column_name = column_token.value
                if not self.is_column_in_table(table_name, column_name):
                    self.collector.val_error(line=column_token.line,
                                             column=column_token.column,
                                             msg=f"Column '{column_name}' in PREDICT clause does not exist in table '{table_name}'.")
            case _:
                pass

    
    def validate_assuming_dict(self, 
                               assuming    : ParsedValue,
                               ptable_name : str) -> None:
        if assuming is None:
            return
        
        if not self.tmp:
            self.collector.val_error(line=assuming.line,
                                     column=assuming.column,
                                     msg="ASSUMING clause is not allowed in static PredQL queries.")
        
        assuming_dict = assuming.value

        self.validate_expr_dict(assuming_dict["Expr"], ptable_name, Context.FROM_ASSUMING)


    def validate_where_dict(self, 
                            where       : ParsedValue,
                            ptable_name : str) -> None:
        if where is None:
            return
        
        where_dict = where.value
        
        self.validate_expr_dict(where_dict["Expr"], ptable_name, Context.FROM_WHERE)

    
    def validate_expr_dict(self, 
                           expr        : ParsedValue | dict,
                           ptable_name : str,
                           context     : Context) -> None:
        if expr is None:
            return
        
        expr_dict = expr.value if isinstance(expr, ParsedValue) else expr
        
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            self.validate_expr_dict(expr_dict["Left"], ptable_name, context)
            self.validate_expr_dict(expr_dict["Right"], ptable_name, context)
        else:
            if isinstance(expr_dict, dict):
                self.validate_cond_dict(expr, ptable_name, context)
            else:
                self.validate_cond_dict(expr_dict, ptable_name, context)
        

    def validate_cond_dict(self, 
                           cond        : ParsedValue,
                           ptable_name : str,
                           context     : Context) -> None:
        if cond is None:
            return
    
        cond_dict = cond.value

        match cond_dict["CondType"]:
            case "aggregation":
                aggr = cond_dict["Aggregation"]
                self.validate_aggr_dict(aggr, ptable_name, context)
                aggr_dict = aggr.value
                aggr_type = aggr_dict["AggrType"].value
                
                # if aggr_type.lower() != "list_distinct":
                #     if classify_token := cond_dict["Classify"]:
                #         self.collector.val_error(line=classify_token.line,
                #                                  column=classify_token.column,
                #                                  msg=f"CLASSIFY modifier is only allowed with LIST_DISTINCT aggregation, found with {aggr_type}.")
                    
                #     if rank_top_token := cond_dict["RankTop"]:
                #         self.collector.val_error(line=rank_top_token.line,
                #                                  column=rank_top_token.column,
                #                                  msg=f"RANK_TOP K modifier is only allowed with LIST_DISTINCT aggregation, found with {aggr_type}.")

                # if K_token := cond_dict["K"]:
                #     K = K_token.value
                #     if K <= 0:
                #         self.collector.val_error(line=K_token.line,
                #                                  column=K_token.column,
                #                                  msg=f"K in RANK_TOP K must be a positive integer, found {K}.")
                
                match cond_dict["CType"]:
                    case "num":
                        if aggr_type.lower() not in AGGR_NUM_COND:
                            self.collector.val_error(line=cond.line,
                                                     column=cond.column,
                                                     msg=f"Aggregation type '{aggr_type}' cannot be used in numeric condition.")
                    case "str":
                        if aggr_type.lower() not in AGGR_STR_COND:
                            self.collector.val_error(line=cond.line,
                                                     column=cond.column,
                                                     msg=f"Aggregation type '{aggr_type}' cannot be used in string condition.")
                    case "null":
                        if aggr_type.lower() not in AGGR_NULL_COND:
                            self.collector.val_error(line=cond.line,
                                                     column=cond.column,
                                                     msg=f"Aggregation type '{aggr_type}' cannot be used in NULL condition.")
                    case _:
                        pass
            case "id_dot_id":
                if self.tmp:
                    self.collector.val_error(line=cond.line,
                                             column=cond.column,
                                             msg="Use SConverter for static predictions.")
                
                table_token = cond_dict["Table"]
                table_name = table_token.value
                if not self.is_table_in_db(table_name):
                    self.collector.val_error(line=table_token.line,
                                             column=table_token.column,
                                             msg=f"Table '{table_name}' in condition does not exist in database.")

                if not self.has_conn_with_main_table(table_name, ptable_name):
                    self.collector.val_error(line=table_token.line,
                                             column=table_token.column,
                                             msg=f"Table '{table_name}' in condition must have a connection with main table '{ptable_name}'.")
                
                # if not self.has_time_col(table_name):
                #     self.collector.val_error(line=table_token.line,
                #                              column=table_token.column,
                #                              msg=f"Table '{table_name}' in condition must have a time column for temporal conditions.")
                    
                column_token = cond_dict["Column"]
                column_name = column_token.value
                if not self.is_column_in_table(table_name, column_name):
                    self.collector.val_error(line=column_token.line,
                                             column=column_token.column,
                                             msg=f"Column '{column_name}' in condition does not exist in table '{table_name}'.")
            case _:
                pass
        

    def validate_aggr_dict(self, 
                           aggr        : ParsedValue,
                           ptable_name : str,
                           context     : Context) -> None:
        if aggr is None:
            return
        
        if not self.tmp:
            self.collector.val_error(line=aggr.line,
                                     column=aggr.column,
                                     msg="Aggregation in static queries is not yer supported.")
            
        aggr_dict = aggr.value

        if where := aggr_dict["Where"]:
            self.collector.val_error(line=where.line,
                                     column=where.column,
                                     msg="WHERE clause in aggregation is not yet supported.")

        table_token = aggr_dict["Table"]
        table_name = table_token.value
        if not self.is_table_in_db(table_name):
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"Table '{table_name}' in aggregation does not exist in database.")

        if not self.has_conn_with_main_table(table_name, ptable_name):
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"Table '{table_name}' in assuming must have a connection with main table '{ptable_name}'.")
        
        if not self.has_time_col(table_name):
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"Table '{table_name}' in aggregation must have a time column for temporal aggregation.")
            
        column_token = aggr_dict["Column"]
        column_name = column_token.value
        if not self.is_column_in_table(table_name, column_name):
            self.collector.val_error(line=column_token.line,
                                     column=column_token.column,
                                     msg=f"Column '{column_name}' in assuming does not exist in table '{table_name}'.")
        
        start_token = aggr_dict["Start"]
        start = int(start_token.value)
        end_token = aggr_dict["End"]
        end = int(end_token.value)

        if start >= end:
            self.collector.val_error(line=start_token.line,
                                     column=start_token.column,
                                     msg=f"Start time must be less than end time in temporal aggregation, found start={start}, end={end}.")
        
        if context == Context.FROM_PREDICT or context == Context.FROM_WHERE:
            if start < 0 or end < 0:
                self.collector.val_error(line=start_token.line,
                                         column=start_token.column,
                                         msg=f"Start and end time in temporal aggregation must be non-negative in PREDICT and WHERE clauses, found start={start}, end={end}.")

        if context == Context.FROM_ASSUMING:
            if start > 0 or end > 0:
                self.collector.val_error(line=start_token.line,
                                         column=start_token.column,
                                         msg=f"Start and end time in temporal aggregation must be non-positive in ASSUMING clause, found start={start}, end={end}.")


    ################## Helper methods ##################
    
    def is_table_in_db(self,
                       table_name : str) -> bool:
        return table_name in self.db.table_dict
    

    def is_column_in_table(self,
                           table_name  : str,
                           column_name : str) -> bool:
        if column_name == "*":
            return True
        
        table = self.db.table_dict.get(table_name)
        if table is None:
            return False
        
        return column_name in table.df.columns
    

    def is_pkey_col(self,
                    table_name  : str,
                    column_name : str) -> bool:
        table = self.db.table_dict.get(table_name)
        if table is None:
            return False
        
        return table.pkey_col == column_name
    

    def has_time_col(self,
                     table_name : str) -> bool:
        table = self.db.table_dict.get(table_name)
        if table is None:
            return False
        return table.time_col is not None


    def has_conn_with_main_table(self,
                                 table_name  : str,
                                 ptable_name : str) -> str:
        if table_name == ptable_name:
            return True
        
        table = self.db.table_dict.get(table_name)
        if table is None:
            return False
        
        for _, pkey_table_name in table.fkey_col_to_pkey_table.items():
            if ptable_name == pkey_table_name:
                return True
        return False
