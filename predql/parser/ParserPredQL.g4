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
    : predict for_each (assuming)? (where)? SEMI_COLUMN
    ;

// ============================================================================
// QUERY CLAUSES
// ============================================================================

// ASSUMING clause: specifies conditions that should be assumed to hold
assuming    
    : ASSUMING expr_or
    ;

// FOR_EACH clause: specifies the table and attribute to iterate over
for_each
    : FOR_EACH ID DOT ID (where)? 
    ;

// PREDICT clause: specifies what to predict (aggregation, expression, or column)
predict
    : PREDICT aggregation (RANK_TOP INT | CLASSIFY)?  
    | PREDICT expr_or 
    | PREDICT ID DOT (ID | STAR) (RANK_TOP INT | CLASSIFY)? 
    ;

// WHERE clause: filters results based on conditions
where
    : WHERE expr_or 
    ;

// ============================================================================
// BOOLEAN EXPRESSIONS (Operator precedence: OR < AND < condition)
// ============================================================================

// OR expressions: lowest precedence
expr_or
    : expr_and (OR expr_and)*
    ;

// AND expressions: medium precedence
expr_and
    : expr_term (AND expr_term)*
    ;

// Terms: highest precedence (conditions or parenthesized expressions)
expr_term
    : condition
    | OPEN_PAREN expr_or CLOSE_PAREN
    ;

// ============================================================================
// CONDITIONS
// ============================================================================

// A condition consists of a subject (aggregation or column reference) and a comparison
condition
    : (NOT)? (aggregation | ID DOT (ID | STAR))  
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
aggregation 
    : AGGR_FUNC OPEN_PAREN ID DOT (ID | STAR) (where)? (COMMA INT COMMA INT (COMMA TIME_MEASURE_UNIT)?)? CLOSE_PAREN
    ;
