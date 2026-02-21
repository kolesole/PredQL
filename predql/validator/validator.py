from abc import ABC, abstractmethod
from enum import auto, Enum, StrEnum

from predql.base import Database
from predql.visitor import ParsedValue

from predql.validator.error import ErrorCollector


AGGR_NUM_COND = {"avg", "count", "count_distinct", "first", "last", "max", "min", "sum"}
AGGR_STR_COND = {"first", "last"}
AGGR_NULL_COND = AGGR_NUM_COND | {"list_distinct"}


class AggrContext(Enum):
    FROM_PREDICT = auto()
    FROM_WHERE = auto()
    FROM_ASSUMING = auto()


class IdDotIdContext(StrEnum):
    FROM_FOR_EACH = "FOR EACH clause"
    FROM_PREDICT = "PREDICT clause"
    FROM_COND = "condition"
    FROM_STAT_AGGR = "static aggregation"
    FROM_TMP_AGGR = "temporal aggregation"


class Validator:
    
    def __init__(self, 
                 collector : ErrorCollector,
                 db        : Database) -> None:
        self.collector = collector
        self.db = db

    
    @abstractmethod
    def validate_query(self, 
                       query : ParsedValue) -> None:
        pass

    @abstractmethod
    def validate_aggr(self, 
                      aggr        : ParsedValue,
                      ptable_name : str,
                      context     : AggrContext) -> None:
        pass

    @abstractmethod
    def validate_id_dot_id(self,
                           table_token  : ParsedValue,
                           column_token : ParsedValue,
                           ptable_name  : str,
                           context      : IdDotIdContext) -> None:
        pass

    
    @abstractmethod
    def validate(self,
                 query_dict : dict) -> None:
        pass
    

    def validate_for_each(self, 
                          for_each : ParsedValue) -> str:
        if for_each is None:
            return None
        
        for_each_dict = for_each.value
        
        table_name = None
        if (table_token := for_each_dict["Table"]) and (column_token := for_each_dict["Column"]):
            table_name = table_token.value
            self.validate_id_dot_id(table_token, column_token, table_name, IdDotIdContext.FROM_FOR_EACH)
            self.validate_where(for_each_dict["Where"], table_name)

        return table_name


    def validate_predict(self, 
                         predict : ParsedValue,
                         ptable_name  : str) -> None:
        if predict is None:
            return
        
        predict_dict = predict.value

        match predict_dict["PredType"]:
            case "aggregation":
                # TODO: ADD STATIC AGGREGATIONS

                aggr = predict_dict["Aggregation"]
                self.validate_aggr(aggr, ptable_name, AggrContext.FROM_PREDICT)

                aggr_dict = aggr.value
                aggr_type = aggr_dict["AggrType"].value
                
                if aggr_type.lower() != "list_distinct":
                    if classify_token := predict_dict["Classify"]:
                        self.collector.val_error(line=classify_token.line,
                                                 column=classify_token.column,
                                                 msg=f"CLASSIFY modifier is only allowed with LIST_DISTINCT aggregation, found with {aggr_type}")
                    
                    if rank_top_token := predict_dict["RankTop"]:
                        self.collector.val_error(line=rank_top_token.line,
                                                 column=rank_top_token.column,
                                                 msg=f"RANK_TOP K modifier is only allowed with LIST_DISTINCT aggregation, found with {aggr_type}")

                if K_token := predict_dict["K"]:
                    K = int(K_token.value)
                    if K <= 0:
                        self.collector.val_error(line=K_token.line,
                                                 column=K_token.column,
                                                 msg=f"K in RANK_TOP K must be a positive integer, found {K}")
            case "expr":
                self.validate_expr(predict_dict["Expr"], ptable_name, AggrContext.FROM_PREDICT)
            case "id_dot_id":
                if self.tmp:
                    self.collector.val_error(line=predict.line,
                                             column=predict.column,
                                             msg="Use SConverter for static predictions")
                
                table_token = predict_dict["Table"]
                column_token = predict_dict["Column"]

                self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_PREDICT)
            case _:
                pass


    def validate_where(self, 
                       where       : ParsedValue,
                       ptable_name : str) -> None:
        if where is None:
            return
        
        where_dict = where.value
        
        self.validate_expr(where_dict["Expr"], ptable_name, AggrContext.FROM_WHERE)

    
    def validate_expr(self, 
                      expr        : ParsedValue | dict,
                      ptable_name : str,
                      context     : AggrContext) -> None:
        if expr is None:
            return
        
        expr_dict = expr.value if isinstance(expr, ParsedValue) else expr
        
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            self.validate_expr(expr_dict["LeftExpr"], ptable_name, context)
            self.validate_expr(expr_dict["RightExpr"], ptable_name, context)
        else:
            if isinstance(expr_dict, dict):
                self.validate_condition(expr, ptable_name, context)
            else:
                self.validate_condition(expr_dict, ptable_name, context)
        

    def validate_condition(self, 
                           condition   : ParsedValue,
                           ptable_name : str,
                           context     : AggrContext) -> None:
        if condition is None:
            return
    
        cond_dict = condition.value

        match cond_dict["CondType"]:
            case "aggregation":
                aggr = cond_dict["Aggregation"]
                self.validate_aggr(aggr, ptable_name, context)
                aggr_dict = aggr.value
                aggr_type = aggr_dict["AggrType"].value
            
                
                match cond_dict["CType"]:
                    case "num":
                        if aggr_type.lower() not in AGGR_NUM_COND:
                            self.collector.val_error(line=condition.line,
                                                     column=condition.column,
                                                     msg=f"Aggregation type '{aggr_type}' cannot be used in numeric condition")
                    case "str":
                        if aggr_type.lower() not in AGGR_STR_COND:
                            self.collector.val_error(line=condition.line,
                                                     column=condition.column,
                                                     msg=f"Aggregation type '{aggr_type}' cannot be used in string condition")
                    case "null":
                        if aggr_type.lower() not in AGGR_NULL_COND:
                            self.collector.val_error(line=condition.line,
                                                     column=condition.column,
                                                     msg=f"Aggregation type '{aggr_type}' cannot be used in NULL condition")
                    case _:
                        pass
            case "id_dot_id":
                table_token = cond_dict["Table"]
                column_token = cond_dict["Column"]

                self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_COND)
            case _:
                pass

    ################## Helper methods ##################
    
    def _is_table_in_db(self, table_name: str) -> bool:
        return table_name.lower() in (name.lower() for name in self.db.table_dict)
    

    def _is_column_in_table(self, table_name: str, column_name: str) -> bool:
        if column_name == "*":
            return True
        table = self.db.table_dict.get(table_name)
        if table is None:
            return False
        return column_name.lower() in (col.lower() for col in table.df.columns)
    

    def _is_pkey_col(self,
                    table_name  : str,
                    column_name : str) -> bool:
        table = self.db.table_dict.get(table_name)
        if table is None:
            return False
        
        return table.pkey_col == column_name
    

    def _has_time_col(self,
                     table_name : str) -> bool:
        table = self.db.table_dict.get(table_name)
        if table is None:
            return False
        return table.time_col is not None


    def _has_conn_with_main_table(self,
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
