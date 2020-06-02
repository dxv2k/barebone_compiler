u'''
In this file, we're going to define grammar structure 
for compiler using yacc 
'''

from ply.yacc as yacc
print('Import yacc successfully')

reserved = {
    'incr': 'INCR', 
    'decr': 'DECR', 
    'clear': 'CLEAR',
}

tokens = ( 
    'NUMBER', 
    'INCR', 
    'DECR', 
    'CLEAR',
)















