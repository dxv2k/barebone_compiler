# This file serve as testing purpose for 
# building lexical analysis for barebone compiler  

import ply.yacc as yacc 
import ply.lex as lex 
from ply.calclex import tokens
print('Import yacc and lex successfully')


# reserved = ( 
#     'clear' : 'CLEAR', 
#     'copy' : 'COPY',
#     'decr' : 'DECR', 
#     'incr' : 'INCR',
#     'do' : 'DO',
#     'init' : 'INIT',
#     'while' : 'WHILE', 
#     NULL : 0, 
#     'to' : 'TO', 
#     'end' : 'END',
#     'not' : 'NOT',
# ) 

# List of tokens
tokens = ( 
     'clear', 
#     'copy',
#     'decr', 
    'incr',
#     'do',
    # 'init',
#     'while', 
#     'NULL', 
#     'to', 
#     'end',
#     'not',
) 

# Ignore spaces and tabs 
t_ignore = ' \t\n'

# Ignore comment, coment started with # 
t_ignore_COMMENT = r'\#.*' 

def t_newline(t): 
    r'\n+' 
    t.lexer.lineno += len(t.value)

def t_error(t): 
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

u'''
# TODO: Some notice here, in order to add action 
# you need to know about yacc and grammar structure 
# Read more about the document, there are tutorials 
'''

def t_clear_stmt(t): 
    r'clear'
    # Missing action 




def t_incr_stmt(t): 
    r'incr'
    # Missing action

# def t_eof(t): 
    # Get more input 


# token rules for variable name 
digit = r'\d+'
alpha = r'[a-zA-Z]'
alpha_num = r'[a-zA-Z_][a-zA-Z0-9_]*' 

# def t_variable(t): 
#     digit 
#     alpha 
#     alpha_num



# Example barebone language
data = '''
clear X; 
'''

# TODO: problem with tokenize ';' 
# TODO: problem with tokenize variable name


lexer = lex.lex()

lexer.input(data)

while True: 
    current_token = lexer.token() 
    if not current_token: 
        break 
    print(current_token)









