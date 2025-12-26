/**
 * Lexer for PredQL (Predictive Query Language)
 * Defines all tokens used in the PredQL grammar
 */
lexer grammar LexerPredQL ;

// ============================================================================
// MAIN FUNCTION KEYWORDS
// ============================================================================

ASSUMING                                          
    : 'ASSUMING' 
    | 'assuming'    
    ;
FOR_EACH
    : ('FOR' | 'for') WS+ ('EACH' | 'each')
    ;
PREDICT 
    : 'PREDICT' 
    | 'predict'
    ;
WHERE
    : 'WHERE' 
    | 'where'
    ;
CLASSIFY
    : 'CLASSIFY' 
    | 'classify'
    ;
RANK_TOP
    : ('RANK' | 'rank') WS+ ('TOP' | 'top')
    ;

// ============================================================================
// AGGREGATION FUNCTIONS
// ============================================================================

AGGR_FUNC   
    : AVG       
    | COUNT 
    | COUNT_DISTINCT
    | FIRST     
    | LAST  
    | LIST_DISTINCT
    | MAX       
    | MIN   
    | SUM
    ;
AVG            
    : 'AVG' 
    | 'avg' 
    ;
COUNT          
    : 'COUNT' 
    | 'count'
    ;
COUNT_DISTINCT 
    : 'COUNT_DISTINCT' 
    | 'count_distinct'
    ;
FIRST          
    : 'FIRST' 
    | 'first' 
    ;
LAST           
    : 'LAST'     
    | 'last'     
    ;
LIST_DISTINCT  
    : 'LIST_DISTINCT'
    | 'list_distinct'
    ;
MAX            
    : 'MAX'      
    | 'max'      
    ;
MIN         
    : 'MIN'      
    | 'min'      
    ;
SUM            
    : 'SUM'      
    | 'sum'      
    ;

// ============================================================================
// COMPARISON OPERATORS
// ============================================================================

// Numerical comparison operators
NUM_COMP_OP 
    : '!='      
    | '<'   
    | '<=' 
    | '=='               
    | '>'       
    | '>='
    ;

// String comparison operators
STR_COMP_OP
    : NOT_LIKE
    | NOT_CONTAINS
    | ENDS_WITH
    | STARTS_WITH
    | LIKE
    | CONTAINS
    | '='
    ;
NOT_LIKE 
    : ('NOT' | 'not') WS+ ('LIKE' | 'like')
    ;
NOT_CONTAINS
    : ('NOT' | 'not') WS+ ('CONTAINS' | 'contains')
    ;
ENDS_WITH
    : ('ENDS' | 'ends') WS+ ('WITH' | 'with')
    ;
STARTS_WITH
    : ('STARTS' | 'starts') WS+ ('WITH' | 'with')
    ;
LIKE
    : ('LIKE' | 'like')
    ;
CONTAINS
    : ('CONTAINS' | 'contains')
    ;

// ============================================================================
// NULL CHECK OPERATORS
// ============================================================================

NULL_CHECK_OP
    : IS_NOT_NULL
    | IS_NULL
    ;
IS_NOT_NULL
    : ('IS' | 'is') WS+ ('NOT' | 'not') WS+ ('NULL' | 'null')
    ;
IS_NULL
    : ('IS' | 'is') WS+ ('NULL' | 'null')
    ;

// ============================================================================
// SPECIAL CHARACTERS AND PUNCTUATION
// ============================================================================

DOT         
    : '.'    
    ;
COMMA       
    : ','
    ;
OPEN_PAREN  
    : '('  
    ;
CLOSE_PAREN 
    : ')' 
    ;
STAR
    : '*'
    ;
SEMI_COLUMN
    : ';'
    ;

// ============================================================================
// LOGICAL OPERATORS
// ============================================================================

AND
    : 'AND'
    | 'and'
    ;
OR
    : 'OR'
    | 'or'
    ;
NOT 
    : 'NOT'
    | 'not'
    ;

// ============================================================================
// BASE DATA TYPES
// ============================================================================

// DateTime in format: YYYY-MM-DD HH:MM:SS
DATETIME
    : DIGIT DIGIT DIGIT DIGIT '-' DIGIT DIGIT '-' DIGIT DIGIT 
      WS                               
      DIGIT DIGIT  DIGIT DIGIT  DIGIT DIGIT 
    ;

// Numeric types (floating point and integers)
FLOAT       
    : DIGIT+ '.' DIGIT*
    | '-' DIGIT+ '.' DIGIT*
    ;
INT         
    : DIGIT+
    | '-' DIGIT+     
    | ('-INF' | '-inf')
    | ('+INF' | '+inf')                    
    ;

// Time measurement units for temporal expressions
TIME_MEASURE_UNIT
    : ('YEARS'   | 'years')
    | ('MONTHS'  | 'months')
    | ('WEEKS'   | 'weeks')
    | ('DAYS'    | 'days')
    | ('HOURS'   | 'hours')
    | ('MINUTES' | 'minutes')
    | ('SECONDS' | 'seconds')
    ;

// String literals with single or double quotes
STRING    
    : SINGLE_QUOTE (~['\\\r\n] | BACKSLASH .)* SINGLE_QUOTE
    | DOUBLE_QUOTE (~['\\\r\n] | BACKSLASH .)* DOUBLE_QUOTE
    ;

// Identifiers (variable names, table names, column names)
ID        
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ; 

// ============================================================================
// WHITESPACE AND CATCH-ALL
// ============================================================================

WS_SKIP        
    : WS+ -> skip 
    ;

// Catch-all for any unrecognized character
ANY                  
    : .
    ;

// ============================================================================
// FRAGMENT DEFINITIONS (Reusable sub-lexical rules)
// ============================================================================

fragment UPPERCASE      : [A-Z]     ;
fragment LOWERCASE      : [a-z]     ;
fragment DIGIT          : [0-9]     ;
fragment WS             : [ \t\r\n] ;
fragment SINGLE_QUOTE   : '\''      ;
fragment DOUBLE_QUOTE   : '"'       ;
fragment BACKSLASH      : '\\'      ;


