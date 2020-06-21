from ply import lex, yacc
print('Import lex  and yacc successfully') 

#-----------------------LEXER--------------------------------

# List of tokens
# Reserved keywords 
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
    "NULL":"0",
} 

tokens = ["IDENT","NUMBER"] + list(reserved.values())
literals = [';','='] 

# Regex rules for tokens 
t_ignore = ' \t\n' # Ignore space,tabs and newline 
t_ignore_COMMENT = r'\#.*' # Ignore comment start with # 

# Rule for identifier (name)
def t_IDENT(t): 
    r'[a-zA-Z_][a-zA-Z_0-9]*' 
    # Not sure this line below 
    t.type = reserved.get(t.value,"IDENT") 
    return t 

def t_NUMBER(t): 
    r'\d+' 
    t.value = int(t.value) 
    try: 
        t.value = int(t.value)
    except ValueError: 
        print("Integer value to large %s" % t.value) 
        t.value = 0
    return t 

def t_newline(t): 
    r'\n+' 
    t.lexer.lineno += len(t.value)

def t_error(t): 
    print("Illegal character '%s'" % t.value[0]) 
    t.lexer.skip(1)

#--------------------------YACC------------------------------------


# def p_init_list_stmt(p): 
#     ''' 
#         init_list_stmt : init_stmt
#                        | init_list stmt_list
#     ''' 

# def p_init_stmt(p): 
#     ''' 
#         init_stmt : INIT var '=' NUMBER ';'
#     ''' 

# def p_stmt_list(p): 
#     ''' 
#         stmt_list : stmt
#                   | stmt_list stmt 
#     ''' 

def p_stmt(p): 
    ''' 
        stmt : clear_stmt 
             | incr_stmt 
             | decr_stmt
    ''' 

def p_var(p): 
    ''' 
        var : IDENT 
    '''

def p_clear_stmt(p): 
    ''' 
        clear_stmt : CLEAR var ';'
    ''' 

def p_incr_stmt(p): 
    ''' 
        incr_stmt : INCR var ';'
    ''' 

def p_decr_stmt(p): 
    ''' 
        decr_stmt : DECR var ';'
    ''' 

# TODO: TEST NEW ERROR CATCHING FUNCTION IN PARSER
def p_error(p): 
    if p: 
        print("Syntax error at '%s'" % p.value)
    else: 
        print("Syntax error at EOF")


# Input testing 
data = ''' 
CLEAR X; 
INCR X; 
''' 
yacc.yacc(debug=True) 
lexer = lex.lex(debug=True) 
lexer.input(data) 
yacc.yacc(debug=True) 
result = yacc.parse(data)
print(result)




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














