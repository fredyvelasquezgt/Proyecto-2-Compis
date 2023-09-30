grammar yapl;


// Definicion lexica

// KEYWORDS
CLASS: 'class' | 'CLASS';
ELSE: 'else' | 'ELSE';
FALSE: 'false';
FI: 'fi' | 'FI';
IF: 'if' | 'IF';
IN: 'in' | 'IN';
INHERITS: 'inherits' | 'INHERITS';
ISVOID: 'isvoid' | 'ISVOID';
LOOP: 'loop' | 'LOOP';
POOL: 'pool' | 'POOL';
THEN: 'then' | 'THEN';
WHILE: 'while' | 'WHILE';
NEW: 'new' | 'NEW';
NOT: 'not' | 'NOT';
TRUE: 'true';
LET: 'let';


TYPE_ID: [A-Z][a-zA-Z0-9_]*|SELF_TYPE;
OBJECT_ID: [a-z][a-zA-Z0-9_]*;
SELF: 'self';
SELF_TYPE: 'SELF_TYPE';
// KEYWORDS: (CLASS|ELSE|FALSE|FI|IF|IN|INHERITS|ISVOID|LOOP|POOL|THEN|WHILE|NEW|NOT|TRUE);
// ID: TYPE_ID | OBJECT_ID ;
STRING              : '"' (ESC | ~ ["\\])* '"' ;
fragment ESC        : '\\' (["\\/bfnrt] | UNICODE) ;
fragment UNICODE    : 'u' HEX HEX HEX HEX ;
fragment HEX        : [0-9a-fA-F] ;

WHITESPACE: (' '|'\n'|'\f'|'\r'|'\t') -> skip;
NEWLINE: [\r\n]+ -> skip;
INT: [0-9]+;
COMMENT: '--' .*? NEWLINE -> skip;
COMMENT_BLOCK: '(*' .*? '*)' -> skip;
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
LT: '<';
LE: '<=';
// ERROR: .;



// Definicion sintatica
prog: (class_def ';')+;

class_def: CLASS TYPE_ID (INHERITS TYPE_ID)? '{' (feature ';')* '}';


feature: OBJECT_ID ('(' (formal ( ',' formal)*)? ')')? ':' TYPE_ID '{' expr '}'                                                 # feat_def
    | OBJECT_ID ':' TYPE_ID ( '<-' expr )?                                                                                      # feat_asgn
;

formal: OBJECT_ID ':' TYPE_ID;
asgn: OBJECT_ID ':' TYPE_ID ( '<-' expr )?;

expr:
    SELF                                                                                                                        # expr_self
    | INT                                                                                                                       # expr_int
    | STRING                                                                                                                    # expr_str
    | TRUE                                                                                                                      # expr_true
    | FALSE                                                                                                                     # expr_false
    | (TYPE_ID | OBJECT_ID)                                                                                                     # expr_id
    | '-' expr                                                                                                                  # expr_negative
    | '~' expr                                                                                                                  # expr_negado
    | NOT expr                                                                                                                  # expr_not
    | NEW TYPE_ID                                                                                                               # expr_instance
    | ISVOID expr                                                                                                               # expr_isvoid
    | '(' expr ')'                                                                                                              # expr_parenthesis
    | '{' (expr ';')+ '}'                                                                                                       # expr_brackets
    | expr (MULT|DIV) expr                                                                                                      # expr_mult
    | expr (PLUS|MINUS) expr                                                                                                    # expr_suma
    | expr (LT|LE) expr                                                                                                         # expr_less_than
    | expr '=' expr                                                                                                             # expr_equal
    | OBJECT_ID '<-' expr                                                                                                       # expr_asgn
    | LET asgn ( ',' asgn )* IN expr                                                                                            # expr_decl
    | expr ('@' TYPE_ID)? '.' OBJECT_ID '(' ( expr (',' expr)* )? ')'                                                           # expr_class_call
    | OBJECT_ID '(' (expr (',' expr)*)? ')'                                                                                     # expr_call
    | IF expr THEN expr ELSE expr FI                                                                                            # expr_if
    | WHILE expr LOOP expr POOL                                                                                                 # expr_while
;
