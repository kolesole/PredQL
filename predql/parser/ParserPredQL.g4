/**
 * Parser for PredQL (Predictive Query Language)
 * Defines the syntax rules for valid PredQL queries
 */
parser grammar ParserPredQL ;

options { tokenVocab=LexerPredQL; }    // Import tokens from the lexer grammar

// ============================================================================
// MAIN QUERY RULE
// ============================================================================

query
    : query_tmp 
    | query_stat
    ;

query_tmp
    : predict_tmp for_each (assuming)? (where_tmp)? SEMICOLON
    ;

query_stat
    : predict_stat for_each (where_stat)? SEMICOLON
    ;

// ============================================================================
// QUERY CLAUSES
// ============================================================================

// FOR_EACH clause: specifies the table and attribute to iterate over
for_each
    : FOR_EACH ID DOT ID (where_stat)?
    ;

// PREDICT clause: specifies what to predict (aggregation, expression, or column)
predict_tmp
    : PREDICT aggregation_tmp (RANK_TOP INT | CLASSIFY)?  
    | PREDICT expr_or_tmp  
    ;

predict_stat
    : PREDICT aggregation_stat (RANK_TOP INT | CLASSIFY)?  
    | PREDICT expr_or_stat  
    | PREDICT ID DOT (ID | STAR)
    ;

// ASSUMING clause: specifies conditions that should be assumed to hold
assuming    
    : ASSUMING expr_or_tmp
    ;

// WHERE clause: filters results based on conditions
where_tmp
    : WHERE expr_or_tmp 
    ;

where_stat
    : WHERE expr_or_stat 
    ;

// ============================================================================
// BOOLEAN EXPRESSIONS (Operator precedence: OR < AND < condition)
// ============================================================================

// OR expressions: lowest precedence
expr_or_tmp
    : expr_and_tmp (OR expr_and_tmp)*
    ;

expr_or_stat
    : expr_and_stat (OR expr_and_stat)*
    ;

// AND expressions: medium precedence
expr_and_tmp
    : expr_term_tmp (AND expr_term_tmp)*
    ;

expr_and_stat
    : expr_term_stat (AND expr_term_stat)*
    ;

// Terms: highest precedence (conditions or parenthesized expressions)
expr_term_tmp
    : condition_tmp
    | OPEN_PAREN expr_or_tmp CLOSE_PAREN
    ;

expr_term_stat
    : condition_stat
    | OPEN_PAREN expr_or_stat CLOSE_PAREN
    ;

// ============================================================================
// CONDITIONS
// ============================================================================

// A condition consists of a subject (aggregation or column reference) and a comparison
condition_tmp
    : (NOT)? aggregation_tmp (num_condition | str_condition | null_check_condition)
    ;

condition_stat
    : (NOT)? (aggregation_stat | ID DOT (ID | STAR))  
      (num_condition | str_condition | null_check_condition)
    ;

// Numeric comparison: compares against numbers or timestamps
num_condition
    : NUM_COMP_OP (DATETIME | FLOAT | INT)
    ;

// String comparison: compares against string values
str_condition
    : STR_COMP_OP STRING 
    ;

// NULL check: tests if a value is NULL or NOT NULL
null_check_condition
    : NULL_CHECK_OP
    ;

// ============================================================================
// AGGREGATION FUNCTIONS
// ============================================================================

// Aggregation format
aggregation_tmp
    : AGGR_FUNC OPEN_PAREN ID DOT (ID | STAR) (where_stat)? COMMA INT COMMA INT COMMA TIME_MEASURE_UNIT CLOSE_PAREN
    ;

aggregation_stat
    : AGGR_FUNC OPEN_PAREN ID DOT (ID | STAR) (where_stat)? CLOSE_PAREN
    ;
