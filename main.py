# from anytree import Node 
# from enum import Enum

# clear_stmt = 'clear' 
# copy_stmt = 'copy' 
# decr_stmt = 'decr'
# incr_stmt = 'incr'
# init_stmt = 'init'
# while_stmt = 'while'


# class Token(object): 
#     def __init__(self,type,value):
#         self.type = type
#         self.value = value        

# filename = 'factorial.bb.txt'

# with open(filename) as f: 
#     program = f.readlines()
    

# currLine = None  # current line of executing program 
#                  # mainly use for error notice purpose

    
class var(): 
    def __init__(self,name,val=0):
        self.name = name 
        self.val = val 
    def getValue(self):
        return self.val 
    def getName(self): 
        return self.name

list_var = []
list_var.append(var('a',4))

str = 'a'

for var in list_var:
    if var.getName() == str: 
        print(True)










