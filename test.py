import ply.yacc as yacc 
import ply.lex as lex
print('import lex and yacc successfully') 


# tokens = ( 
#     'clear', 
#     'copy',
#     'decr', 
#     'incr',
#     'do',
#     'init',
#     'while', 
#     'NULL', 
#     'to', 
#     'end',
#     'not',
# ) 

tokens = ( 
    'NUMBER', 
    'PLUS', 
    'MINUS', 
    'TIMES', 
    'DIVIDE', 
    'LPAREN',
    'RPAREN',
)

# Regular expression rules with simple tokens 
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


# A string containing ignored characters (spaces and tabs) 
t_ignore = ' \t'

# Regular expression with some action code 
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

# Build lexer
lexer = lex.lex()


# Test 
data = ''' 
3 + 4 * 10 
  + -20 * 2
'''

lexer.input(data)

#Tokenize 
while True: 
    current_token = lexer.token()
    if not current_token: 
        break 
    print(current_token)







