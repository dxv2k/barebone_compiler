# u'''
# '''

# import ply.lex as lex 
# # import ply.yacc as yacc 
# print('Import lex successfully')

# u''' 
# Read here first 
# The problem with the scanner right is that 
# it cannot detect keyword statement (init,clear,incr,...)
# but mistaken with variable name (X,absd,...)
# In order to so do, you'll have to figure out 
# how to made it detect keyword first 
# if it doesn't match -> going to detect variable name 

# '''


# # List of tokens 
# tokens = ( 
#     'INIT',
#     'CLEAR',
#     'INCR',
#     'VAR', 
#     # 'NUMBER',
# )

# # Tokens ignored by compiler
# t_ignore = ' \t' # Ignore space and tabs
# t_ignore_COMMENT = r'\#.*' 

# # Token for variable name
# t_INCR = r'incr'
# t_CLEAR = r'clear' 
# t_INIT = r'init'
# # t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'

# def t_NUMBER(t): 
#     r'\d+' 
#     t.value = int(t.value) 
#     return t


# # This structure here is very simple 
# # only detect matching keywords
# # def t_CLEAR(t): 
# #     r'clear'
# #     # Missing action 

# # def t_INCR(t): 
# #     r'incr'

# # def t_INIT(t): 
# #     r'init'
# #     # Missing action 

# def t_newline(t): 
#     r'\n+'
#     t.lexer.lineno += len(t.value)

# def t_error(t): 
#     print("Illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)

# # Build the lexer 
# # lexer = lex.lex(debug=True)
# lexer = lex.lex()

# data = '''
# clear X
# init A
# '''

# # Pass input to lexer
# lexer.input(data)

# # Tokenize
# while True: 
#     current_token = lexer.token() 
#     if not current_token: 
#         break 
#     print(current_token)

u''' 

'''


import ply.yacc as yacc 
import ply.lex as lex
print('Import lex successfully')

# reserverd = { 
#     'init': 'INIT', 
#     'decr': 'DECR'
# }

tokens = ( 
    'NUMBER',
    'PLUS'
)

# Simple regular expression rules
t_PLUS = r'\+'

# Tokens ignored by compiler
t_ignore = ' \t' # Ignore space and tabs
t_ignore_COMMENT = r'\#.*' 

# Regex with action code 
# Regex recognize number
def t_NUMBER(t): 
    r'\d+'
    t.value = int(t.value) 
    return t

def t_newline(t): 
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t): 
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

digit = r'([0-9])'
nondigit = r'(_A-Za-z])' 
identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'

from ply.lex import TOKEN
@TOKEN(identifier)
def t_ID(t): 
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

lexer = lex.lex(debug=True)
data = '''
1+2  
'''
lexer.input(data)

while True: 
    current_token = lexer.token() 
    if not current_token: 
        break 
    print(current_token)

