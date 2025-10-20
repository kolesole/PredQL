lexer grammar Lexer_PQL ;

/******************* FRAGMENTS *******************/
/*************************************************/
fragment UPPERCASE      : [A-Z]                   ;
fragment LOWERCASE      : [a-z]                   ;
fragment DIGIT          : [0-9]                   ;
fragment WS             : [ \t\r\n]               ;
fragment SINGLE_QUOTE   : '\''                    ;
fragment DOUBLE_QUOTE   : '"'                     ;
fragment BACKSLASH      : '\\'                    ;
/*************************************************/
/*************************************************/


/******************* TOKENS **********************/
/*************************************************/
/* DECLARATION OF SPECIAL TOKENS (KEYWORDS/FUNCTIONS) */
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
/******************************************************/
/* AGGREGATION FUNCTIONS */
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
/*************************/    

/* GROUPS OF BOOLEAN OPERATIONS */
/* the second argument is a number */
NUM_COMP_OP 
    : '!='      
    | '<'   
    | '<=' 
    | '=='               // in kumo.ai '=' 
    | '>'       
    | '>='
    ;

/* the second argument is a string */
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

/* null check operations */
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

/* logical operations */
LOGICAL_OP
    : AND
    | OR
    ;
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
/********************************/ 

/* NUMBERS */
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
/***********/  

/* SOME CHARACTERS */
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

/*******************/

/* FOR USE IN COMPARISONS */
STRING    
    : SINGLE_QUOTE (~['\\\r\n] | BACKSLASH .)* SINGLE_QUOTE
    | DOUBLE_QUOTE (~['\\\r\n] | BACKSLASH .)* DOUBLE_QUOTE
    ;
    
/* FOR TABLE AND COLUMN NAMES */
ID        
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ; 

/* SKIP WHITESPACE */
WS_SKIP        
    : WS+ -> skip 
    ;

/* CATCH ALL TOKENS WHICH ARE NOT YET DEFINED */
ANY                  
    : .
    ;

/*************************************************/
/*************************************************/


