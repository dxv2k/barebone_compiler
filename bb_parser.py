from ply import lex, yacc
print('Import lex  and yacc successfully') 

#-----------------------LEXER--------------------------------

# List of tokens
reserved = { 
    'init':'INIT', 
    'clear':'CLEAR', 
    "while":"WHILE", 
    "do":"DO", 
    "incr":"INCR", 
    "decr":"DECR", 
    "copy":"COPY", 
    "to":"TO", 
    "not":"NOT", 
} 

tokens = ["IDENT","NUMBER"] + list(reserved.values())
literals = [';','='] 

# Regex rules for tokens 
t_ignore = ' \t' 
t_ignore_COMMENT = r'\#.*'  
 
def t_ID(t): 
    r'[a-zA-Z_][a-zA-Z_0-9]*' 
    t.type = reserved.get(t.value,"IDENT")
    return t 

def t_NUMBER(t): 
    r'\d+' 
    t.value = int(t.value) 
    return t 

def t_newline(t): 
    r'\n+' 
    t.lexer.lineno += len(t.value)

def t_error(t): 
    print("Illegal character '%s'" % t.value[0]) 


#--------------------------YACC------------------------------------

def p_stmt(p): 
    ''' 
        stmt : clear_stmt 
             | incr_stmt
    ''' 

def p_clear_stmt(p): 
    ''' 
        clear_stmt : CLEAR IDENT ';'
    ''' 

def p_incr_stmt(p): 
    ''' 
        incr_stmt : INCR IDENT ';'
    '''

def p_factor(p): 
    ''' 
        factor : NUMBER 
               | IDENT 
    ''' 

#def p_error(p): 
#    if p:
#        print("Syntax error at line",p.lineno)
#        # print('Syntax error at line' )
#    else: 
#        print('Reached unexpected EOF')



data = '''
clear X;
incr X;
hello 
''' 

# lex.lex(debug=True) 
# yacc.yacc(debug=True) 
lexer = lex.lex(debug=True) 
lexer.input(data) 
while True: 
    current_token = lexer.token() 
    if not current_token: 
        break 
    print(current_token)

yacc.yacc(debug=True) 
result = yacc.parse(data)
print(result)



# TODO: Add p_error()
#def p_error(p): 
#    print("Syntax error input")

#Testing lexer 
# data = '''
# 12 
# thisIsVariable
# incr X 
# decr X
# # Ignore this line
# # Ignore this line too
# while X not 0 do  
# not
# ; 
# = 
# ''' 

# lexer = lex.lex() 
# lexer.input(data) 
# while True: 
#     current_token = lexer.token() 
#     if not current_token: 
#         break 
#     print(current_token)














#------------------------INTERPRETER-------------------------
# class INTERPRETER(): 














