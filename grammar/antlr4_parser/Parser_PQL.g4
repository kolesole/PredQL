parser grammar Parser_PQL ;

options { tokenVocab=Lexer_PQL; }    // import tokens from the lexer grammar

query
    : predict for_each (assuming)? (where)?  SEMI_COLUMN
    ;
    
assuming    
    : ASSUMING expr_or
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
    : WHERE expr_or 
    ;

expr_or
    : expr_and (OR expr_and)*
    ;

expr_and
    : expr_term (AND expr_term)*
    ;

expr_term
    : condition
    | OPEN_PAREN expr_or CLOSE_PAREN
    ;

condition
    : (NOT)? (aggregation | ID DOT (ID | STAR))  
      (num_condition | str_condition | null_check_condition)
    ;
// nezapomenout se zeptat o NOT
num_condition
    : NUM_COMP_OP (DATETIME | FLOAT | INT)
    ;

str_condition
    : STR_COMP_OP STRING 
    ;

null_check_condition
    : NULL_CHECK_OP
    ;

aggregation 
    : AGGR_FUNC OPEN_PAREN ID DOT (ID | STAR) (where)? (COMMA INT COMMA INT (COMMA TIME_MEASURE_UNIT)?)? CLOSE_PAREN
    ;
