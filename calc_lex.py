import ply.lex as lex 
import ply.yacc as yacc
from ply.lex import TOKEN
print('Import lex successfully')


# List of tokens name 
# REQUIRED 
tokens = ( 
    'NUMBER', 
    'PLUS', 
    'MINUS', 
    'TIMES', 
    'DIVIDE', 
    'LPAREN', 
    'RPAREN',
)

# Specified tokens 
# Regular expression rules for simple tokens 
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

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

# def t_COMMENT(t): 
#     r'\#.*' # '#' will be the comment symbol for the program
#     pass # No return value  

digit = r'([0-9])'
nondigit = r'([_A-Za-z])'
identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'
 
@TOKEN(identifier) 
def t_ID(t): 
    t.value = (t.value, symbol_lookup(t.value))
    return t



# Build the lexer
# lexer = lex.lex(debug=True)
lexer = lex.lex()

data = ''' 
3 + 4 * 10
+ -20 * 2
'''

# Pass input to lexer
lexer.input(data)

# Tokenize
while True: 
    current_token = lexer.token() 
    if not current_token: 
        break 
    print(current_token)






