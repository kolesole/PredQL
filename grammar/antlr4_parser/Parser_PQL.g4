parser grammar Parser_PQL ;

options { tokenVocab=Lexer_PQL; }    // import tokens from the lexer grammar

query
    : help_query+ SEMI_COLUMN
    ;

help_query
    : assuming 
    | for_each 
    | predict 
    | where
    ;
    
assuming    
    : ASSUMING condition (LOGICAL_OP condition)* 
    ;

for_each
    : FOR_EACH ID DOT ID (where)? 
    ;

predict
    : PREDICT aggregation (RANK_TOP INT | CLASSIFY)? 
    | PREDICT condition (RANK_TOP INT | CLASSIFY)?
    | PREDICT ID DOT (ID | STAR) (RANK_TOP INT | CLASSIFY)? 
    ;
    
where
    : WHERE condition (LOGICAL_OP condition)* 
    ;

condition
    : num_condition
    | str_condition
    | null_check_condition
    ;

num_condition
    : aggregation NUM_COMP_OP (FLOAT | INT)
    | ID DOT (ID | STAR) NUM_COMP_OP (DATETIME | FLOAT | INT)
    ;

str_condition
    : aggregation STR_COMP_OP STRING
    | ID DOT (ID | STAR) STR_COMP_OP STRING
    ;

null_check_condition
    : aggregation NULL_CHECK_OP
    | ID DOT (ID | STAR) NULL_CHECK_OP
    ;

aggregation 
    : AGGR_FUNC OPEN_PAREN ID DOT (ID | STAR) (where)? (COMMA INT COMMA INT (COMMA TIME_MEASURE_UNIT)?)? CLOSE_PAREN
    ;
