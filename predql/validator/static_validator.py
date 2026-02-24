"""Static query validator class for PredQL."""

from predql.base import Database
from predql.visitor import ParsedValue

from predql.validator.error import ErrorCollector
from predql.validator.validator import AggrContext, IdDotIdContext, Validator


class SValidator(Validator):
    r"""Validator for static (non-temporal) PredQL queries.
    
    Implements abstract methods from the base *`Validator`* class.
    """
    
    def __init__(self,
                 collector : ErrorCollector,
                 db        : Database) -> None:
        super().__init__(collector, db)
    

    def validate(self, 
                 query_dict : dict) -> None:
        r"""Validates a parsed query dictionary.
        
        Ensures the query is static (not temporal) and delegates to validate_query.
        
        Args:
            query_dict (dict): Parsed query dictionary from the visitor.
        
        Returns:
            out (None):
        """
        # check if the query is static
        if query := query_dict["QueryStat"]:
            self.validate_query(query)
        elif query := query_dict["QueryTmp"]:
            self.collector.val_error(line=query.line,
                                     column=query.column,
                                     msg="For static converter, only static queries are supported, found temporal query")
        
    
    def validate_query(self,
                       query : ParsedValue) -> None:
        r"""Validates all components of a static query.
        
        Args:
            query (ParsedValue): Parsed static query to validate.

        Returns:
            out (None):
        """
        if query is None:
            return
        
        query_dict = query.value
        # validate FOR EACH clause and get parent table name
        # if FOR EACH is not present -> end validation
        # otherwisr -> validate PREDICT AND WHERE clauses
        if ptable_name := self.validate_for_each(query_dict["ForEach"]):
            self.validate_predict(query_dict["Predict"], ptable_name)
            self.validate_where(query_dict["Where"], ptable_name)
    
    
    def validate_aggregation(self,
                             aggr        : ParsedValue,
                             ptable_name : str,
                             context     : AggrContext) -> None:
        r"""Validates a static aggregation.
        
        Args:
            aggr (ParsedValue): Parsed aggregation to validate.
            ptable_name (str): Name of the parent table.
            context (AggrContext): Context where the aggregation appears.  
                Does not affect validation logic for static queries.
        
        Returns:
            out (None):
        """
        if aggr is None:
            return
            
        aggr_dict = aggr.value

        table_token = aggr_dict["Table"]
        column_token = aggr_dict["Column"]

        # validate WHERE clause inside the aggregation if present
        if where := aggr_dict["Where"]:
            self.validate_where(where, table_token.value)

        # validate table.column in the aggregation
        self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_STAT_AGGR)
    

    def validate_id_dot_id(self,
                           table_token  : ParsedValue,
                           column_token : ParsedValue,
                           ptable_name  : str,
                           context      : str) -> None:
        r"""Validates a table.column reference in a static query.
        
        Checks that the table exists, is connected to the parent table,
        and that the column exists in that table.
        
        Args:
            table_token (ParsedValue): Parsed table name.
            column_token (ParsedValue): Parsed column name.
            ptable_name (str): Name of the parent table.
            context (str): Context where this reference appears.
        
        Returns:
            out (None):
        """
        table_name = table_token.value
        
        # check table existence
        if not self._is_table_in_db(table_name):
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"Table '{table_name}' in {context} does not exist in database")
        
        # check table relationship with parent    
        if not self._has_conn_with_main_table(table_name, ptable_name):
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"Table '{table_name}' in {context} is not connected to main table '{ptable_name}'")
        
        # check column existence
        column_name = column_token.value
        if not self._is_column_in_table(table_name, column_name):
            self.collector.val_error(line=column_token.line,
                                     column=column_token.column,
                                     msg=f"Column '{column_name}' in {context} does not exist in table '{table_name}'")
        
        # FOR EACH requires a primary key column
        if context == IdDotIdContext.FROM_FOR_EACH and not self._is_pkey_col(table_name, column_name):
            self.collector.val_error(line=column_token.line,
                                     column=column_token.column,
                                     msg=f"Column '{column_name}' in {context} is not a primary key column of table '{table_name}'")
        
        # static aggregations are not yet fully supported
        if context == IdDotIdContext.FROM_STAT_AGGR:
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"!!!! STATIC AGGREGATION IS NOT SUPPORTED YET !!!!")
