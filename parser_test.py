from ply import lex,yacc 

# List of tokens 
tokens = [ 
    "ID",
    "NUMBER", 
    "PLUS",
    "MINUS",
    "MULT",
    "DIV",
    "LPAREN", 
    "RPAREN",
]

#-------------------REGEX-RULES------------------------------
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t): 
    r'\d+' 
    t.value = int(t.value)
    return t 

# Set for simple regex rules for tokenizer
t_ignore = ' \t' 
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\(' 
t_RPAREN = r'\)' 

# Tracking lines for multiple line streaming input
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Lex error handling 
def t_error(t): 
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#---------------------GRAMMAR-RULES------------------------------
# expr : expr PLUS term
#      | expr MINUS term 
#      | term 
# term : temr MULTI factor
#      | temr DIV factor 
#      | factor
# factor : NUMBER
#        | ( expr )            





# Build lex 
lexer = lex.lex()


# Testing lex
data = ''' 
32 + 10
12 - 4
12 * 8
X
( )
( X )
X124
_123abas
/asba
'''

lexer.input(data)


# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
 








