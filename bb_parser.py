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

tokens = ["ID","NUMBER"] + list(reserved.values())
literals = [';','='] # not sure this working 

# Regex rules for tokens 
t_ignore = ' \t' 
t_ignore_COMMENT = r'\#.*'  
 
def t_ID(t): 
    r'[a-zA-Z_][a-zA-Z_0-9]*' 
    t.type = reserved.get(t.value,"ID")
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

# def p_program(p): 
#     ''' 
#         program : stmt_list | init_list stmt_list
#     ''' 

# def p_init_list(p): 
#     ''' 
#         init_list : init  | init_list init 
#     ''' 

# def p_init(p): 
#     ''' 
#        init : INIT ID '=' NUMBER ';'  
#     ''' 

# def p_stmt_list(p): 
#     ''' 
#         stmt_list : stmt | stmt_list stmt
#     ''' 

# Full rule of grammar 
# def p_stmt(p): 
#     ''' 
#         stmt : clear_stmt | incr_stmt | decr_stmt | while_stmt | copy_stmt
#     ''' 

# def p_factor(p): 
#     ''' 
#         factor : ID
#                | NUMBER
#     ''' 

# def p_clear_stmt(p): 
#     ''' 
#         clear_stmt : CLEAR ID ';'
#     ''' 

# def p_incr_stmt(p): 
#     ''' 
#         incr_stmt : INCR ID ';' 
#     ''' 

# def p_decr_stmt(p): 
#     ''' 
#         decr_stmt : DECR ID ';' 
#     ''' 

# def p_while_stmt(p): 
#     ''' 
#         while_stmt : WHILE ID NOT NUMBER DO stmt_list ';'
#     '''

# def p_copy_stmt(p): 
#     ''' 
#         copy_stmt : COPY ID TO ID ';'
#     ''' 

def p_factor(p): 
    ''' 
        factor : NUMBER | ID 
    ''' 


def p_error(p): 
    if p:
        print("error at line ",p.lineno)
        # print('Syntax error at line' )
    else: 
        print('Reached unexpected EOF')

data = '1' 

lex.lex(debug=True) 
# yacc.yacc(debug=True) 
yacc.yacc() 
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














