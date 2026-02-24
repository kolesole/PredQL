"""Container for parsed values with location information."""

class ParsedValue:
    r"""Wrapper for parsed values that preserves their source location.
    
    Used by the visitor to attach line and column information to values  
    extracted from the parse tree. 
    """

    def __init__(self, 
                 value  : dict | str, 
                 line   : int, 
                 column : int) -> None:
        r"""Initializes a *`ParsedValue`* object with a value and its location.
        
        Args:
            value (str): The parsed value from the query.
            line (int): Source line number.
            column (int): Source column number.
        
        Returns:
            out (None):
        """
        self.value = value
        self.line = line
        self.column = column
    

    def __repr__(self) -> str:
        r"""Returns a string representation showing value and location.
        
        Returns:
            out (str): Formatted string with value and its position in source.
        """
        return f"{self.value} at line {self.line}:{self.column})"
