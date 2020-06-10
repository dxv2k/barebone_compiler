from ply import lex,yacc  
print('Import lex and yacc successfully')

# List of tokens 
tokens = [ 
    "PLUS"
    "MINUS", 
    "ID",
    "NUMBER",
    # "MULT",
] 

# List of regex rules for tokens 

# TODO: ADD t_ignore_COMMENT
t_PLUS = r"\+"
t_MINUS = r"-"
t_ID = r"^[a-zA-Z]+$"
t_NUMBER = r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?"



# t_MULT = r"\*"
t_ignore = r" \t" # Ignore spaces and tabs

# TODO: add t_LPAREN, t_RPAREN



def t_error(t): 
    print("Illegal characters '%s'" % t.value[0]) 
    t.lexer.skip(1)

#-------------------------PARSER---------------------------
# Grammar rules: 
# P -> E 
# E -> E + T | T 
# T -> T * F | F 
# F -> ( E ) | ID

# def p_stmt(p): 
#     '''
#         stmt : expr
#     '''

# def p_expr(p): 
#     ''' 
#         expr : expr PLUS term 
#              | term 
#     '''

# def p_term(p): 
#     ''' 
#         term : term MULT factor
#              | factor
#     ''' 

# # def p_factor(p): 
    



# Testing for lexer (tokenizer) 
data = ''' 32 + 10 ''' 


# Build the lexer 
lexer = lex.lex(debug=True)
lexer.input(data)
while True: 
    curr_token = lexer.token()
    if not curr_token: 
        break 
    print(curr_token)


