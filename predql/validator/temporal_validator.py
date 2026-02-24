"""Temporal query validator class for PredQL."""

from predql.base import Database
from predql.visitor import ParsedValue

from predql.validator.error import ErrorCollector
from predql.validator.validator import AggrContext, IdDotIdContext, Validator


class TValidator(Validator):
    r"""Validator for temporal PredQL queries.
    
    Implements abstract methods from the base *`Validator`* class.  
    In addition, implements validation logic for ASSUMING clause.
    """
    
    def __init__(self,
                 collector : ErrorCollector,
                 db        : Database) -> None:
        super().__init__(collector, db)
    
    
    def validate(self,
                 query_dict : dict) -> None:
        r"""Validates a parsed query dictionary.
        
        Ensures the query is temporal (not static) and delegates to validate_query.
        
        Args:
            query_dict (dict): Parsed query dictionary from the visitor.
        
        Returns:
            out (None):
        """
        # check if the query is temporal
        if query := query_dict["QueryTmp"]:
            self.validate_query(query)
        elif query := query_dict["QueryStat"]:
            self.collector.val_error(line=query.line,
                                     column=query.column,
                                     msg="For temporal converter, only temporal queries are supported, found static query")
        

    def validate_query(self,
                       query : ParsedValue) -> None:
        r"""Validate all components of a temporal query.
        
        Args:
            query (ParsedValue): Parsed temporal query to validate.
        
        Returns:
            out (None):
        """
        if query is None:
            return
        
        query_dict = query.value
        # validate FOR EACH clause and get parent table name
        # if FOR EACH is not present -> end validation
        # otherwisr -> validate PREDICT, ASSUMING, and WHERE clauses
        if ptable_name := self.validate_for_each(query_dict["ForEach"]):
            self.validate_predict(query_dict["Predict"], ptable_name)
            self.validate_assuming(query_dict["Assuming"], ptable_name)
            self.validate_where(query_dict["Where"], ptable_name)
    

    def validate_aggregation(self,
                             aggr        : ParsedValue,
                             ptable_name : str,
                             context     : AggrContext) -> None:
        r"""Validate a temporal aggregation with time window constraints.

        Checks that:
        - Start < End
        - Time ranges are non-negative in PREDICT or WHERE
        - Time ranges are non-positive in ASSUMING (looking backward)
        
        Args:
            aggr (ParsedValue): Parsed aggregation to validate.
            ptable_name (str): Name of the parent table.
            context (AggrContext): Context where the aggregation appears.
        
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
        self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_TMP_AGGR)
        
        # validate temporal window constraints
        start_token = aggr_dict["Start"]
        start = int(start_token.value)
        end_token = aggr_dict["End"]
        end = int(end_token.value)

        # start time must be less than end time
        if start >= end:
            self.collector.val_error(line=start_token.line,
                                     column=start_token.column,
                                     msg=f"Start time must be less than end time in temporal aggregation, found start={start}, end={end}")
        
        # PREDICT and WHERE look forward in time (non-negative range)
        if context in [AggrContext.FROM_PREDICT, AggrContext.FROM_WHERE]:
            if start < 0 or end < 0:
                self.collector.val_error(line=start_token.line,
                                         column=start_token.column,
                                         msg=f"Start and end time in temporal aggregation must be non-negative in PREDICT and WHERE clauses, found start={start}, end={end}")

        # ASSUMING looks backward in time (non-positive range)
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
        """Validates a table.column reference in a temporal query.
        
        In addition to static checks, ensures temporal aggregation tables
        have a time column defined(only for references from aggregations).
        
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
        
        # temporal aggregations require a time column
        if context == IdDotIdContext.FROM_TMP_AGGR and not self._has_time_col(table_name):
            self.collector.val_error(line=table_token.line,
                                     column=table_token.column,
                                     msg=f"Table '{table_name}' in {context} does not have a time column")
        
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


    def validate_assuming(self, 
                         assuming    : ParsedValue,
                         ptable_name : str) -> None:
        r"""Validate ASSUMING clause.
        
        Just passes the context to `validate_expr` function.
        
        Args:
            assuming (ParsedValue): Parsed ASSUMING clause.
            ptable_name (str): Name of the parent table.
        
        Returns:
            out (None):
        """
        if assuming is None:
            return
        
        assuming_dict = assuming.value
        
        self.validate_expr(assuming_dict["Expr"], ptable_name, AggrContext.FROM_ASSUMING)
