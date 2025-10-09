parser grammar Parser_PQL ;

options { tokenVocab=Lexer_PQL; }    // import tokens from the lexer grammar

aggregation 
    : AGGR_FUNC OPEN_PAREN ID DOT ID COMMA INT COMMA INT CLOSE_PAREN 
    ;

condition
    : num_condition
    | str_condition
    | null_check_condition
    ;

num_condition
    : aggregation NUM_COMP_OP NUM
    ;

str_condition
    : aggregation STR_COMP_OP STRING
    ;

null_check_condition
    : aggregation NULL_CHECK_OP
    ;

assuming    
    : ASSUMING condition (LOGICAL_OP condition)*
    ;

for_each
    : FOR_EACH ID DOT ID
    ;

predict
    : PREDICT aggregation
    | PREDICT ID DOT ID
    ;




