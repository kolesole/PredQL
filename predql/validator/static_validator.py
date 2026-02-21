from predql.base import Database
from predql.validator.validator import Validator, ErrorCollector, AggrContext, IdDotIdContext
from predql.visitor import ParsedValue

class SValidator(Validator):
    def __init__(self,
                 collector : ErrorCollector,
                 db        : Database) -> None:
        super().__init__(collector, db)
    
    def validate(self, 
                 query_dict : dict) -> None:
        if query := query_dict["QueryStat"]:
            self.validate_query(query)
        elif query := query_dict["QueryTmp"]:
            self.collector.val_error(line=query.line,
                                     column=query.column,
                                     msg="For static converter, only static queries are supported, found temporal query")
        
    
    def validate_query(self,
                       query : ParsedValue) -> None:
        if query is None:
            return
        
        query_dict = query.value
        if ptable_name := self.validate_for_each(query_dict["ForEach"]):
            self.validate_predict(query_dict["Predict"], ptable_name)
            self.validate_where(query_dict["Where"], ptable_name)
    
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

        self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_STAT_AGGR)
    

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

        
