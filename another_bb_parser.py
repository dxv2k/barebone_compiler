from ply import lex,yacc 
print('Import lex and yacc successfully') 

tokens = [
    "IDENT", 
    "NUMBER",
]

literals = [';']

# Regex rules for tokens 
t_ignore = ' \t\n' # Ignore space,tabs and newline 
t_ignore_COMMENT = r'\#.*' # Ignore comment start with # 

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

data = ''' 
# Ignore this line
secondVariable;
thisIsVariable;
''' 

def p_stmt(p): 
    ''' 
        stmt : var 
    '''

def p_var(p): 
    ''' 
        var : IDENT ';'
    '''

def p_expr(p): 
    ''' 
        expr : var 
             | stmt
    '''

# lexer = lex.lex()
# lexer.input(data) 
# while True: 
#     current_token = lexer.token() 
#     if not current_token: 
#         break 
#     print(current_token)


lexer = lex.lex(debug=True) 
lexer.input(data) 
yacc.yacc(debug=True) 
result = yacc.parse(data)
print(result)










