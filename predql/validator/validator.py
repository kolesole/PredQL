from abc import abstractmethod

from predql.base import Database, Table
from predql.validator import Error, ErrorCollector
from predql.visitor import ParsedValue

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
                               for_each_dict : dict) -> str:
        if for_each_dict is None:
            return

        table_token = for_each_dict["Table"]
        table_name = table_token.value
        table = self.db[table_name]
        if table is None:
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"Table '{table_name}' in FOR EACH clause does not exist in database.")

        column_token = for_each_dict["Column"]
        column_name = column_token.value
        if column_name != "*":
            if column_name not in table.df.columns:
                self.collector.val_error(line=column_token.line,
                                        column=column_token.column,
                                        msg=f"Column '{column_name}' in FOR EACH clause does not exist in table '{table_name}'.")
            
            if column_name != table.pkey_col:
                self.collector.val_error(line=column_token.line,
                                        column=column_token.column,
                                        msg=f"Column '{column_name}' in FOR EACH clause must be a primary key column of table '{table_name}'.")
        
        # if where := for_each_dict["Where"]:
        #     self.collector.val_error(line=where.line,
        #                              column=where.column,
        #                              msg="WHERE clause in FOR EACH is not yet supported.")
        #TODO: WHERE validation

        return table_token.value
    
    def validate_predict_dict(self, 
                         predict_dict : dict,
                         ptable_name  : str) -> None:
        if predict_dict is None:
            return
        
        match predict_dict["QType"]:
            case "aggregation":
                pass
            case "expr":
                # expr = predict_dict["Expr"]
                # self.collector.val_error(line=expr.line,
                #                          column=expr.column,
                #                          msg="Expression prediction is not yet supported.")
                #TODO: EXPR validation
                pass
            case "id_dot_id":
                pass
            case _:
                pass

        

    
    def validate_assuming_dict(self, 
                          assuming_dict : dict,
                          ptable_name   : str) -> None:
        if assuming_dict is None:
            return
        
        if not self.tmp:
            # self.collector.val_error(line=assuming.line,
            #                          column=assuming.column,
            #                          msg="ASSUMING clause is not allowed in static PredQL queries.")
            #TODO: ASSUMING validation
            pass
        
        self.validate_expr_dict(assuming_dict["Expr"], ptable_name, True)


    def validate_where_dict(self, 
                            where_dict  : dict,
                            ptable_name : str) -> None:
        if where_dict is None:
            return
        
        self.validate_expr_dict(where_dict["Expr"], ptable_name, False)

    def validate_expr_dict(self, 
                         expr_dict   : dict,
                         ptable_name : str,
                         in_assuming : bool) -> None:
        if expr_dict is None:
            return
        
        if "Op" in expr_dict:
            self.validate_expr(expr_dict["Left"], ptable_name, in_assuming)
            self.validate_expr(expr_dict["Right"], ptable_name, in_assuming)
        else:
            self.validate_cond_dict(expr_dict, ptable_name, in_assuming)
        

    def validate_cond_dict(self, 
                           cond_dict   : dict,
                           ptable_name : str,
                           in_assuming : bool) -> None:
        pass

    def validate_num_cond_dict(self, 
                               num_cond_dict : dict,
                               ptable_name   : str) -> None:
        pass

    def validate_str_cond_dict(self, 
                          str_cond_dict : dict,
                          ptable_name   : str) -> None:
        pass

    def validate_null_cond_dict(self, 
                                null_cond_dict : dict,
                                ptable_name    : str) -> None:
        pass

    def validate_aggr_dict(self, 
                           aggr_dict   : dict,
                           ptable_name : str) -> None:
        pass

    def validate_id_dot_id(self, 
                           table       : ParsedValue,
                           column      : ParsedValue,
                           ptable_name : str) -> None:
        pass

    def pkey_table2fkey_col(self,
                            ptable_name : str) -> str:
        for fkey_col_name, pkey_table_name in self.fkey_col_to_pkey_table.items():
            if ptable_name == pkey_table_name:
                return fkey_col_name
        return None
