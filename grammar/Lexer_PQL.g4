lexer grammar Lexer_PQL ;

/******************* FRAGMENTS *******************/
/*************************************************/
fragment UPPERCASE      : [A-Z]                   ;
fragment LOWERCASE      : [a-z]                   ;
fragment DIGIT          : [0-9]                   ;
fragment SINGLE_QUOTE   : '\''                    ;
fragment DOUBLE_QUOTE   : '"'                     ;
fragment BACKSLASH      : '\\'                    ;


/* AGGREGATION OPERATIONS */
fragment AVG            : 'AVG'      | 'avg'      ;
fragment COUNT          : 'COUNT'    | 'count'    ;
fragment COUNT_DISTINCT : 'COUNT_DISTINCT'      
                        | 'count_distinct'        ;
fragment FIRST          : 'FIRST'    | 'first'    ;
fragment LAST           : 'LAST'     | 'last'     ;
fragment LIST_DISTINCT  : 'LIST_DISTINCT'
                        | 'list_distinct'         ;
fragment MAX            : 'MAX'      | 'max'      ;
fragment MIN            : 'MIN'      | 'min'      ;
fragment SUM            : 'SUM'      | 'sum'      ;

/* BOOLEAN OPERATIONS OR THEIR PARTS */
fragment AND            : 'AND'      | 'and'      ;
fragment CONTAINS       : 'CONTAINS' | 'contains' ;  // not  contains

/**** ENDS WITH ****/
fragment ENDS           : 'ENDS'     | 'ends'     ;
fragment WITH           : 'WITH'     | 'with'     ;
/*******************/

/** IS {NOT} NULL **/
fragment IS             : 'IS'       | 'is'       ;
fragment NOT            : 'NOT'      | 'not'      ;
fragment NULL           : 'NULL'     | 'null'     ;
/*******************/

fragment LIKE           : 'LIKE'     | 'like'     ;  // not like
fragment OR             : 'OR'       | 'or'       ;

/*** STARTS WITH ***/
fragment STARTS         : 'STARTS'   | 'starts'   ;
// WITH is already in ENDS WITH part
/*******************/

/** PARTS OF SPECIAL TOKENS **/
/**** FOR EACH *****/
fragment FOR            : 'FOR'      | 'for'      ;
fragment EACH           : 'EACH'     | 'each'     ;
/*******************/

/**** RANK TOP *****/
fragment RANK           : 'RANK'     | 'rank'     ;
fragment TOP            : 'TOP'      | 'top'      ; 
/*******************/
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
    : FOR EACH
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
    : RANK TOP
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
    : LIKE
    | NOT LIKE 
    | CONTAINS 
    | NOT CONTAINS
    | ENDS WITH
    | STARTS WITH
    ;

NULL_CHECK_OP
    : IS NULL
    | IS NOT NULL
    ;

LOGICAL_OP
    : AND
    | OR
    ;        

NOT_OP
    : NOT
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
    ;
NUM         
    : FLOAT     
    | INT                     
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
WS        
    : [ \t\r\n]+ -> skip 
    ;

/* CATCH ALL TOKENS WHICH ARE NOT YET DEFINED */
ANY                  
    : .
    ;

/*************************************************/
/*************************************************/


