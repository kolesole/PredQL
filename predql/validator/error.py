from antlr4.error.ErrorListener import ErrorListener

class Error():
    
    def __init__(self, 
                 line    : int,
                 column  : int,
                 message : str) -> None:
        
        self.line = line
        self.column = column
        self.message = message
    
    def __str__(self) -> str:
        return f"{Colors.RED}{Colors.BOLD}ERROR{Colors.DEFAULT} at line {self.line}:{self.column} - {Colors.UNDERLINE}{self.message}{Colors.DEFAULT}"


class ErrorCollector(ErrorListener):

    def __init__(self) -> None:
        super().__init__()
        self.errors = []
    
    def syntaxError(self, 
                    recognizer      : any, 
                    offendingSymbol : any,
                    line            : int, 
                    column          : int, 
                    msg             : str, 
                    e               : any) -> None:
        
        self.errors.append(Error(line, column, msg))
    
    def val_error(self, 
                  line   : int, 
                  column : int, 
                  msg    : str) -> None:
        
        self.errors.append(Error(line, column, msg))
    
    def __repr__(self) -> str:
        return "\n".join(f"{i+1}. " + str(error) for i, error in enumerate(self.errors))
    
    def __len__(self) -> int:
        return len(self.errors)


class Colors:
    DEFAULT = '\033[0m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'