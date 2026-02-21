from predql.base import Database
from predql.validator.validator import Validator, ErrorCollector, AggrContext, IdDotIdContext
from predql.visitor import ParsedValue

class TValidator(Validator):
    def __init__(self,
                 collector : ErrorCollector,
                 db        : Database) -> None:
        super().__init__(collector, db)
    
    
    def validate(self,
                 query_dict : dict) -> None:
        if query := query_dict["QueryTmp"]:
            self.validate_query(query)
        elif query := query_dict["QueryStat"]:
            self.collector.val_error(line=query.line,
                                     column=query.column,
                                     msg="For temporal converter, only temporal queries are supported, found static query")
        

    def validate_query(self,
                       query : ParsedValue) -> None:
        if query is None:
            return
        
        query_dict = query.value
        if ptable_name := self.validate_for_each(query_dict["ForEach"]):
            self.validate_predict(query_dict["Predict"], ptable_name)
            self.validate_assuming(query_dict["Assuming"], ptable_name)
            self.validate_where(query_dict["Where"], ptable_name)


    def validate_assuming(self, 
                         assuming    : ParsedValue,
                         ptable_name : str) -> None:
        if assuming is None:
            return
        
        assuming_dict = assuming.value
        
        self.validate_expr(assuming_dict["Expr"], ptable_name, AggrContext.FROM_ASSUMING)


    def validate_aggregation(self,
                             aggr        : ParsedValue,
                             ptable_name : str,
                             context     : AggrContext) -> None:
        if aggr is None:
            return
            
        aggr_dict = aggr.value

        table_token = aggr_dict["Table"]
        column_token = aggr_dict["Column"]

        if where := aggr_dict["Where"]:
            self.validate_where(where, table_token.value)

        self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_AGGR)
        
        start_token = aggr_dict["Start"]
        start = int(start_token.value)
        end_token = aggr_dict["End"]
        end = int(end_token.value)

        if start >= end:
            self.collector.val_error(line=start_token.line,
                                     column=start_token.column,
                                     msg=f"Start time must be less than end time in temporal aggregation, found start={start}, end={end}")
        
        if context in [AggrContext.FROM_PREDICT, AggrContext.FROM_WHERE]:
            if start < 0 or end < 0:
                self.collector.val_error(line=start_token.line,
                                         column=start_token.column,
                                         msg=f"Start and end time in temporal aggregation must be non-negative in PREDICT and WHERE clauses, found start={start}, end={end}")

        if context == AggrContext.FROM_ASSUMING:
            if start > 0 or end > 0:
                self.collector.val_error(line=start_token.line,
                                         column=start_token.column,
                                         msg=f"Start and end time in temporal aggregation must be non-positive in ASSUMING clause, found start={start}, end={end}")


    def validate_id_dot_id(self,
                           table_token  : ParsedValue,
                           column_token : ParsedValue,
                           ptable_name  : str,
                           context      : str) -> None:
        table_name = table_token.value
        if not self._is_table_in_db(table_name):
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"Table '{table_name}' in {context} does not exist in database")
            
        if not self._has_conn_with_main_table(table_name, ptable_name):
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"Table '{table_name}' in {context} is not connected to main table '{ptable_name}'")
        
        if context == IdDotIdContext.FROM_TMP_AGGR and not self._has_time_col(table_name):
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"Table '{table_name}' in {context} does not have a time column")
        
        column_name = column_token.value
        if not self._is_column_in_table(table_name, column_name):
            self.collector.val_error(line=column_token.line,
                                     column=column_token.column,
                                     msg=f"Column '{column_name}' in {context} does not exist in table '{table_name}'")
        
        
        if context == IdDotIdContext.FROM_FOR_EACH and not self._is_pkey_col(table_name, column_name):
            self.collector.val_error(line=column_token.line,
                                     column=column_token.column,
                                     msg=f"Column '{column_name}' in {context} is not a primary key column of table '{table_name}'")
        
        if context == IdDotIdContext.FROM_STAT_AGGR:
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"!!!! STATIC AGGREGATION IS NOT SUPPORTED YET !!!!")

        
