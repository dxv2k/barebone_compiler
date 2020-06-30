from ply import lex, yacc
print('Import lex and yacc successfully') 

#-----------------------LEXER--------------------------------
# List of tokens
# Reserved keywords 
reserved = { 
    "init":"INIT", 
    "clear":"CLEAR", 
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
t_ignore_COMMENT = r'\#.*' # Ignore comment start with  

# Rule for identifier (name)
def t_IDENT(t): 
    r'[a-zA-Z_][a-zA-Z_0-9]*' 
    # Check in reserved keywords first
    t.type = reserved.get(t.value,"IDENT") 
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
def p_init_stmt(p): 
    ''' 
        init_stmt : INIT var '=' NUMBER ';'
    '''
    find_var(p[2])
    print(p[4])

# def p_assign_stmt(p): 
#     '''
#     '''

def p_clear_stmt(p): 
    ''' 
        clear_stmt : CLEAR var ';'
    '''
    # print(p[0])
    # print(p[1])
    print(p[2])

def p_var(p): 
    # Default initial value of variable will be None 
    # Ex: clear X 
    # -> list_var = {'X':None}
    # NOTICE: None value will only be apply here
    ''' 
        var : IDENT
    '''     
    find_var(p[1])


list_var = {} # Contains list of VAR name and its VALUE
def find_var(input_var): 
    u''' 
        find_var(var) will search for variable names 
        that are in used
        If variable doesn't exists then init variable with 
        0 value
    '''
    for var in list_var: 
        if var == input_var: 
            print('Variable name already exists') 
            break
    # If variable doesn't exists -> init_zero
    list_var[input_var] = 0



# TODO: add def p_error(p)
# def p_error(p): 
#     if p: 
#         print("Syntax error at '%s'" % p.value)
#     else: 
#         print("Syntax error at EOF")




# Input testing 
data = ''' 
clear X; 
init X = 100; 
# Ignore this line for testing purpose 
''' 

lexer = lex.lex(debug=True) 
lexer.input(data) 
yacc.yacc(debug=True) 
result = yacc.parse(data)
print(result)


# lexer = lex.lex() 
# lexer.input(data) 
# while True: 
#     current_token = lexer.token() 
#     if not current_token: 
#         break 
#     print(current_token)


#------------------------INTERPRETER-------------------------
# class INTERPRETER(): 














