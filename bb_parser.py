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
    # Check in reserved keywords first if exists
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
             | init_stmt
    '''

def p_init_stmt(p): 
    ''' 
        init_stmt : INIT var '=' NUMBER ';'
    '''
    # If var isn't exists 
    if isVarExists(p[2]) == False: 
        set_var(p[2],p[4])
    else:  
        print('Do not allow the same variable to initialize multiple times')

# NOT WORKING ON clear_stmt
def p_clear_stmt(p): 
    ''' 
        clear_stmt : CLEAR var ';'
    '''
    # DO NOT ALLOW to use clear_stmt to intialize variable
    if isVarExists(p[2]) == False: 
        print("Variable '%s' must be initialize first" % p[2])
    else: 
        set_var(p[2])
def p_var(p): 
    # Default initial value of variable will be None 
    # Ex: clear X 
    # -> list_var = {'X':None}
    # NOTICE: None value will only be apply here
    ''' 
        var : IDENT
    '''     
    p[0] = p[1] # assign 'IDENT' from tokenizer to 'var'


# Contains list of VAR name and its VALUE
list_var = {} 

def set_var(var_name, var_value=0): 
    u'''
        set_var(
            var_name: STRING variable name 
            var_value: INTEGER  
        )
        - Used to set variable name and its value 
        - This can also be used to initialize variable 
    '''
    # Directly set variable name and value to dictionary 
    # This is not a good way but still I'm gonna do it
    list_var[var_name] = var_value

def isVarExists(input_var): 
    u''' 
        isVarExists(var) will search for variable names 
        that are in used
        If variable doesn't exists then init variable with 
        0 value
    '''
    # Find if variable DO NOT exists on program 
    if input_var not in list_var.keys():   
        return False 
    else: return True

    # try: 
    #     for var in list_var: 
    #         if var == input_var: 
    #             print('Variable name already exists') 
    #             return var
    # except: 
    #     print("Variable '%s' must be initialize " % input_var)
    # If variable doesn't exists -> init_zero
    # list_var[input_var] = 0

# TODO: add def p_error(p)
# def p_error(p): 
#     if p: 
#         print("Syntax error at '%s'" % p.value)
#     else: 
#         print("Syntax error at EOF")


# TESTING WITH NO CONSOLE INPUT
# Input testing 
data = ''' 
# Ignore this line for testing purpose 
init X = 12;
clear X;
''' 
lexer = lex.lex() 
lexer.input(data) 
parser = yacc.yacc() 
result = parser.parse(data,lexer)
print(result)
print(list_var)

# # TESTING WITH CONSOLE INPUT
# # Multiple time input 
# lexer = lex.lex() 
# parser = yacc.yacc() 
# while 1: 
#     try: 
#         # input() supports for Python3 but not sure with Python2
#         s = input('>>> ')
#     except EOFError: 
#         break 
#     if not s : continue
#     parser.parse(s,lexer)

# # TESTING TOKENIZER
# data = ''' 
# init X = 12;
# '''
# lexer = lex.lex() 
# lexer.input(data) 
# while True: 
#     current_token = lexer.token() 
#     if not current_token: 
#         break 
#     print(current_token)


#------------------------INTERPRETER-------------------------
# def INTERPRETER(): 


