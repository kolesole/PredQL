"""Base validator module for PredQL query validation."""

from abc import ABC, abstractmethod
from enum import auto, Enum, StrEnum

from predql.base import Database, Table
from predql.visitor import ParsedValue

from predql.validator.error import ErrorCollector

# aggregation types that can be used with numeric conditions
AGGR_NUM_COND = {"avg", "count", "count_distinct", "first", "last", "max", "min", "sum"}

# aggregation types that can be used with string conditions
AGGR_STR_COND = {"first", "last"}

# aggregation types that can be used with NULL checks conditions
AGGR_NULL_COND = AGGR_NUM_COND | {"list_distinct"}


class AggrContext(Enum):
    r"""Context indicating where an aggregation appears in the query.
    
    Used for context-specific validation rules (e.g., temporal ranges  
    must be non-negative in PREDICT but non-positive in ASSUMING).
    """
    FROM_PREDICT = auto()
    FROM_WHERE = auto()
    FROM_ASSUMING = auto()


class IdDotIdContext(StrEnum):
    r"""Context indicating where a table.column reference appears.
    
    Provides descriptive strings for error messages when validating  
    table.column references in different parts of the query.
    """
    FROM_FOR_EACH = "FOR EACH clause"
    FROM_PREDICT = "PREDICT clause"
    FROM_COND = "condition"
    FROM_STAT_AGGR = "static aggregation"
    FROM_TMP_AGGR = "temporal aggregation"


class Validator(ABC):
    r"""Base abstract validator for PredQL queries.
    
    Provides common validation logic for both static and temporal queries.
    """
    
    def __init__(self, 
                 collector : ErrorCollector,
                 db        : Database) -> None:
        """Initializes the validator with an error collector and database.
        
        Args:
            collector (ErrorCollector): *`ErrorCollector`* to accumulate validation errors.
            db (Database): *`Database`* instance containing schema information.
        
        Returns:
            out (None):
        """
        self.collector = collector
        self.db = db


    @abstractmethod
    def validate(self,
                 query_dict : dict) -> None:
        """Top-level validation entry point.
        
        Note:
            For explanation of the validation process, see concrete subclasses.
        """
        pass


    @abstractmethod
    def validate_query(self, 
                       query : ParsedValue) -> None:
        r"""Validates the entire query structure.
        
        Note:
            For explanation of the validation process, see concrete subclasses.
        """
        pass


    @abstractmethod
    def validate_aggregation(self, 
                             aggr        : ParsedValue,
                             ptable_name : str,
                             context     : AggrContext) -> None:
        r"""Validates an aggregation expression.
        
        Note:
            For explanation of the validation process, see concrete subclasses.
        """
        pass


    @abstractmethod
    def validate_id_dot_id(self,
                           table_token  : ParsedValue,
                           column_token : ParsedValue,
                           ptable_name  : str,
                           context      : IdDotIdContext) -> None:
        r"""Validates a table.column reference.
        
        Note:
            For explanation of the validation process, see concrete subclasses.
        """
        pass
    

    def validate_for_each(self, 
                          for_each : ParsedValue) -> str | None:
        r"""Validates FOR EACH clause and returns the parent table name.
        
        Args:
            for_each (ParsedValue): Parsed FOR EACH clause.
        
        Returns:
            table_name (str): Name of the parent table, or None if FOR EACH is not present.
        """
        if for_each is None:
            return None
        
        for_each_dict = for_each.value
        
        # if table or column tokens are not presented -> exit from for each validation
        # otherwise -> validate table.column and WHERE clause
        table_name = None
        if (table_token := for_each_dict["Table"]) and (column_token := for_each_dict["Column"]):
            table_name = table_token.value
            # validate that the table.column reference is valid
            self.validate_id_dot_id(table_token, column_token, table_name, IdDotIdContext.FROM_FOR_EACH)
            # validate WHERE clause
            self.validate_where(for_each_dict["Where"], table_name)

        return table_name


    def validate_predict(self, 
                         predict : ParsedValue,
                         ptable_name  : str) -> None:
        r"""Validates PREDICT clause.
        
        Args:
            predict (ParsedValue): Parsed PREDICT clause.
            ptable_name (str): Name of the parent table.
        
        Returns:
            out (None):
        """
        if predict is None:
            return
        
        predict_dict = predict.value

        match predict_dict["PredType"]:
            case "aggregation":
                # TODO: ADD STATIC AGGREGATIONS
                # validate aggregation and its components
                aggr = predict_dict["Aggregation"]
                self.validate_aggregation(aggr, ptable_name, AggrContext.FROM_PREDICT)

                aggr_dict = aggr.value
                aggr_type = aggr_dict["AggrType"].value
                
                # LIST_DISTINCT is the only aggregation that supports CLASSIFY and RANK_TOP
                if aggr_type.lower() != "list_distinct":
                    if classify_token := predict_dict["Classify"]:
                        self.collector.val_error(line=classify_token.line,
                                                 column=classify_token.column,
                                                 msg=f"CLASSIFY modifier is only allowed with LIST_DISTINCT aggregation, found with {aggr_type}")
                    
                    if rank_top_token := predict_dict["RankTop"]:
                        self.collector.val_error(line=rank_top_token.line,
                                                 column=rank_top_token.column,
                                                 msg=f"RANK_TOP K modifier is only allowed with LIST_DISTINCT aggregation, found with {aggr_type}")

                # Validate K parameter if RANK_TOP is present
                if K_token := predict_dict["K"]:
                    K = int(K_token.value)
                    if K <= 0:
                        self.collector.val_error(line=K_token.line,
                                                 column=K_token.column,
                                                 msg=f"K in RANK_TOP K must be a positive integer, found {K}")
            case "expr":
                # validate boolean expression in PREDICT
                self.validate_expr(predict_dict["Expr"], ptable_name, AggrContext.FROM_PREDICT)
            case "id_dot_id":
                # static queries can predict table.column directly
                table_token = predict_dict["Table"]
                column_token = predict_dict["Column"]
                # validate table.column reference
                self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_PREDICT)
            case _:
                pass


    def validate_where(self, 
                       where       : ParsedValue,
                       ptable_name : str) -> None:
        r"""Validates WHERE clause.
        
        Just passes the context to `validate_expr` function.

        Args:
            where (ParsedValue): Parsed WHERE clause.
            ptable_name (str): Name of the parent table.
        
        Returns: 
            out (None):
        """
        if where is None:
            return
        
        where_dict = where.value
        
        self.validate_expr(where_dict["Expr"], ptable_name, AggrContext.FROM_WHERE)

    
    def validate_expr(self, 
                      expr        : ParsedValue | dict,
                      ptable_name : str,
                      context     : AggrContext) -> None:
        r"""Validates a boolean expression (recursively handles AND/OR).
        
        Args:
            expr (ParsedValue | dict): Parsed expression to validate.
            ptable_name (str): Name of the parent table.
            context (AggrContext): Context where the expression appears.
        """
        if expr is None:
            return
        
        # unwrap ParsedValue if necessary
        expr_dict = expr.value if isinstance(expr, ParsedValue) else expr
        
        # if expression has an operator (AND/OR), recursively validate both sides
        if isinstance(expr_dict, dict) and "Op" in expr_dict:
            self.validate_expr(expr_dict["LeftExpr"], ptable_name, context)
            self.validate_expr(expr_dict["RightExpr"], ptable_name, context)
        else:
            # base case: validate a single condition
            if isinstance(expr_dict, dict):
                self.validate_condition(expr, ptable_name, context)
            else:
                self.validate_condition(expr_dict, ptable_name, context)
        

    def validate_condition(self, 
                           condition   : ParsedValue,
                           ptable_name : str,
                           context     : AggrContext) -> None:
        r"""Validates a single condition.

        Ensures that aggregation types are compatible with the comparison operators.
        
        Args:
            condition (ParsedValue): Parsed condition to validate.
            ptable_name (str): Name of the parent table.
            context (AggrContext): Context where the condition appears.
        
        Returns:
            out (None):
        """
        if condition is None:
            return
    
        cond_dict = condition.value

        match cond_dict["CondType"]:
            case "aggregation":
                # validate the aggregation and its components
                aggr = cond_dict["Aggregation"]
                self.validate_aggregation(aggr, ptable_name, context)
                aggr_dict = aggr.value
                aggr_type = aggr_dict["AggrType"].value
            
                # Validate that the aggregation type is compatible with the condition type
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
                # validate table.column reference
                self.validate_id_dot_id(table_token, column_token, ptable_name, IdDotIdContext.FROM_COND)
            case _:
                pass

    ################## Helper methods ##################

    def _get_table_case_insensitive(self, 
                                    table_name: str) -> Table | None:
        r"""Retrieves *`Table`* object from the database using case-insensitive table name.
        
        Args:
            table_name (str): Name of the table to retrieve.
        Returns:
            out (Table): *`Table`* object corresponding to the given name, or None if not found.
        """
        if not (table_dict := self.db.table_dict):
            return None

        # k ... name of the table
        # v ... Table object
        for k, v in table_dict.items():
            if k.lower() == table_name.lower():
                return v
        
        return None
    
    
    def _is_table_in_db(self, 
                        table_name: str) -> bool:
        r"""Checks if a table exists in the database (case-insensitive).
        
        Args:
            table_name (str): Name of the table to check.
        
        Returns:
            out (bool): True if the table exists, False otherwise.
        """
        table = self._get_table_case_insensitive(table_name)
        
        return table is not None
    

    def _is_column_in_table(self, 
                            table_name: str, 
                            column_name: str) -> bool:
        r"""Checks if a column exists in a table (case-insensitive).
        
        Args:
            table_name (str): Name of the table.
            column_name (str): Name of the column to check ('*' is always valid).
        
        Returns:
            bool: True if the column exists or is '*', False otherwise.
        """
        if column_name == "*":
            return True
        
        if not (table := self._get_table_case_insensitive(table_name)):
            return False
        
        # k ... name of the column
        return column_name.lower() in (k.lower() for k in table.df)
    

    def _is_pkey_col(self,
                    table_name  : str,
                    column_name : str) -> bool:
        r"""Checks if a column is the primary key of a table.
        
        Args:
            table_name (str): Name of the table.
            column_name (str): Name of the column to check.
        
        Returns:
            bool: True if the column is the primary key, False otherwise.
        """
        if not (table := self._get_table_case_insensitive(table_name)):
            return False
        
        if not (pkey_col := table.pkey_col):
            return False
        
        return pkey_col.lower() == column_name.lower()
    

    def _has_time_col(self,
                     table_name : str) -> bool:
        r"""Checks if a table has a time column.
        
        Args:
            table_name (str): Name of the table to check.
        
        Returns:
            bool: True if the table has a time column, False otherwise.
        """
        if not (table := self._get_table_case_insensitive(table_name)):
            return False
        
        return table.time_col is not None


    def _has_conn_with_main_table(self,
                                 table_name  : str,
                                 ptable_name : str) -> bool:
        r"""Checks if a table is connected to the parent table via foreign key.
        
        Args:
            table_name (str): Name of the child table to check.
            ptable_name (str): Name of the parent table.
        
        Returns:
            bool: True if the table is the parent itself or has a foreign key
                referencing it, False otherwise.
        """
        if table_name.lower() == ptable_name.lower():
            return True

        if not (table := self._get_table_case_insensitive(table_name)):
            return False

        if not (fkey_col_to_pkey_table := table.fkey_col_to_pkey_table):
            return False
        
        # k ... name of the foreign key column
        # v ... name of the parent table that the foreign key references
        for k, v in fkey_col_to_pkey_table.items():
            if ptable_name.lower() == v.lower():
                return True
            
        return False
