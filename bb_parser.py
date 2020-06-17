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

# tokens = [ 
#     "ID", 
#     "NUMBER", 
#     "INIT", 
#     "CLEAR", 
#     "WHILE", 
#     "DO", 
#     "INCR", 
#     "DECR", 
#     "COPY", 
#     "TO" 
# ]

# Regex rules for tokens 
t_ignore = ' \t' 
t_ignore_COMMENT = r'\#.*'  
#t_INIT = r'init' 
#t_CLEAR = r'clear' 
#t_WHILE = r'while' 
#t_DO = r'do' 
#t_INCR = r'incr' 
#t_DECR = r'decr' 
#t_COPY = r'copy' 
#t_TO = r'TO' 

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





#Testing lexer 
data = '''
12 
thisIsVariable
incr X 
decr X
# Ignore this line
# Ignore this line too
while X not 0 do  
not
''' 

lexer = lex.lex() 
lexer.input(data) 
while True: 
    current_token = lexer.token() 
    if not current_token: 
        break 
    print(current_token)



