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
'''
    Identifier regex rules can't catch illegal variable name
    like \aszfas 
    It consider its as tokens 
''' 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*' #TODO: check regex var name rules
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
# stmt : expr 
# expr : expr PLUS term
#      | expr MINUS term 
#      | term 
# term : term MULT factor
#      | term DIV factor 
#      | factor
# factor : NUMBER
#        | ( expr )            
# TODO: consider to add identifier rule for factor?  



#TODO: Add list_stmt 
#TODO: Add stmt 

#def p_list_stmt(p): 
#    ''' 
#        list_stmt : stmt
#    ''' 

def p_stmt(p): 
    '''
        stmt : expr
    ''' 
    p[0] = ('stmt',p[1])

def p_expr(p): 
    '''
        expr : expr PLUS term
             | expr MINUS term 
             | term 
    ''' 
    if (len(p) == 2): 
        p[0] = p[1] 
    p[0] = ("expr",p[0],p[1])

def p_term(p): 
    ''' 
        term : term MULT factor
             | term DIV factor 
             | factor
    ''' 

def p_factor(p):  
    ''' 
        factor : NUMBER
               | expr             
    ''' 

## Testing lex
#data = ''' 
#32 + 10
#12 - 4
#12 * 8
#X
#( )
#( X )
#X124
#_123abas
#/asba
#'''

# Build lex 
# lexer = lex.lex()


# lexer.input(data)


# Tokenize
#while True:
#    tok = lexer.token()
#    if not tok: 
#        break      # No more input
#    print(tok)
 
# Testing data for parser  
data = '32 + 10' 
lex.lex()
yacc.yacc() 
result = yacc.parse(data) 
print(result)








