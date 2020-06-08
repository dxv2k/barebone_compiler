from ply import lex,yacc 
print('Import lex and yacc successfully')

tokens = [ 
   # Variable (identifier)
   'identifier',
   
   # Basic commands 
   'incr', 
   'decr', 
   'init', 
   'clear',
   
   # while loop command

   # copy command
]

for idx,keyword in enumerate(tokens): 
   tokens[idx] = keyword.upper()

for keyword in tokens: 
   print(keyword)


# Set of simple regular expression rules 
# literals = [';'] # used for end of line
t_ignore_COMMENT = r'\#.*'
t_ignore = r' \t'
t_identifier = r"^[a-zA-Z]+$"
t_number = r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?"

# def t_incr(): 
#    r'\incr'

# def t_decr(): 
#    r'\decr'

# def t_init(): 
#    r'\init'

# def t_clear(): 
#    r'\clear'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()