from anytree import Node 
from enum import Enum

clear_stmt = 'clear' 
copy_stmt = 'copy' 
decr_stmt = 'decr'
incr_stmt = 'incr'
init_stmt = 'init'
while_stmt = 'while'


class Token(object): 
    def __init__(self,type,value):
        self.type = type
        self.value = value        

# class Interpreter(obecjt): 







filename = 'factorial.bb.txt'

with open(filename) as f: 
    program = f.readlines()
    





currLine = None  # current line of executing program 
                 # mainly use for error notice purpose

    


























