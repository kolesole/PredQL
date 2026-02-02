class ParsedValue:

    def __init__(self, 
                 value  : any, 
                 line   : int, 
                 column : int) -> None:
        self.value  = value
        self.line   = line
        self.column = column
    

    def __repr__(self) -> str:
        return f"{self.value} at line {self.line}:{self.column})"
