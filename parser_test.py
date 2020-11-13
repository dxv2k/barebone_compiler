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
    "COMMENT",
]

#-------------------REGEX-RULES------------------------------
'''
    Identifier regex rules can't catch illegal variable name
    like \aszfas 
    It consider its as tokens 
''' 
#TODO:  add support for block comment 
#def t_structed_comment(t): 

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*' #TODO: check regex var name rules
    return t

def t_NUMBER(t): 
    r'\d+' 
    t.value = int(t.value)
    return t 

# Set for simple regex rules for tokenizer
t_ignore = ' \t' 
t_ignore_COMMENT = r'\#.*'  
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
# list_stmt : list_stmt | stmt # This need to be re-consider 
# stmt : expr 
# expr : expr PLUS term
#      | expr MINUS term 
#      | term 
## term : term MULT factor
#      | term DIV factor 
#      | factor
# factor : NUMBER
#        | '(' expr ')'            
# TODO: consider to add identifier rule for factor?  



#TODO: Add list_stmt 
# NOT WORKING 
#def p_init_list(p): 
#    ''' 
#        init : init_list  
#             | init
#    ''' 
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
    if (len(p) == 2): 
        p[0] = p[1] 
    p[0] = ("term",p[0],p[1])
        
def p_factor(p):  
    ''' 
        factor : ID 
               | '(' expr ')'             
    ''' 

# def p_error(p):
#     if p:
#         raise BaseException("Syntax error at line " + str(p.lineno))
#     else:
#         raise BaseException("Reached unexpected end of file.")


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



# Testing data for parser  
data = '''
32 + 10
100 - 10
42 / 50
42 * 50
# ignore this whole line 
# ignore this line too 
thisIsVariable
''' 


lex.lex(debug=True)
# yacc.yacc(debug=True) 
yacc.yacc() 
result = yacc.parse(data) 
print(result)


## Build lex 
#lexer = lex.lex()
#lexer.input(data)
## Tokenize
#while True:
#    tok = lexer.token()
#    if not tok: 
#        break      # No more input
#    print(tok)
#

#-------------------ABSTRACT SYNTAX TREE---------------------------














#----------------------------INTERPRETER---------------------------

# class Interpreter(): 
# 








