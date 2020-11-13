from ply import lex,yacc

tokens = [ 
    'clear'
]

t_clear = r'CLEAR'
t_ignore = ' \t\n' # Ignore space,tabs and newline 
t_ignore_COMMENT = r'\#.*' # Ignore comment start with # 

# Input testing 
data = ''' 
CLEAR X;
''' 

lexer = lex.lex() 
lexer.input(data) 
while True: 
    current_token = lexer.token() 
    if not current_token: 
        break 
    print(current_token)











