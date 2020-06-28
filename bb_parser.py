from ply import lex, yacc
print('Import lex and yacc successfully') 

#-----------------------LEXER--------------------------------
# List of tokens
# Reserved keywords 
reserved = { 
    "init":"INIT", 
    # "clear":"CLEAR", 
    "while":"WHILE", 
    "do":"DO", 
    "incr":"INCR", 
    "decr":"DECR", 
    "copy":"COPY", 
    "to":"TO", 
    "not":"NOT",
    "NULL":"0",
    # TODO: Add token for <,>,= comparision  
} 

tokens = ["IDENT","NUMBER"] + list(reserved.values())
literals = [';','='] 

# Regex rules for tokens 
t_ignore = ' \t\n' # Ignore space,tabs and newline 
t_ignore_COMMENT = r'\#.*' # Ignore comment start with # 
t_clear = r'CLEAR'

# Rule for identifier (name)
def t_IDENT(t): 
    r'[a-zA-Z_][a-zA-Z_0-9]*' 
    # Check in reserved keywords first
    # t.type = reserved.get(t.value,"IDENT") 
    return t 

# t_NUMBER will be used as INTEGER
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

def p_stmt(p): 
    ''' 
        stmt : clear_stmt
    '''

def p_clear_stmt(p): 
    ''' 
        clear_stmt : CLEAR var ';'
    '''
    p[0] = ('clear_stmt',p[2]) 

def p_var(p): 
    ''' 
        var : IDENT
    '''     
    print(p[0])


# Input testing 
data = ''' 
CLEAR X;
''' 

# lexer = lex.lex(debug=True) 
# lexer.input(data) 
# yacc.yacc(debug=True) 
# result = yacc.parse(data)
# print(result)


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

lexer = lex.lex() 
lexer.input(data) 
while True: 
    current_token = lexer.token() 
    if not current_token: 
        break 
    print(current_token)


#------------------------INTERPRETER-------------------------
# class INTERPRETER(): 














