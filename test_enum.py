# Testing enum for stmt_type in barebone_compiler
from enum import Enum,auto 

class stmt_type(Enum): 
    u'''
    '''
    # TODO: not sure should include init_stmt  
    clear_stmt = auto() 
    incr_stmt = auto() 
    decr_stmt = auto() 
    while_stmt = auto() 
    copy_stmt = auto() 
    add_clear_stmt = auto() 

class stmt(self): 
    u'''
    '''
    def __init__(
                line=None, # use for tracking statement line 
                type=None, # stmt_type passthrough here  
                var=None, # variable name 
    ): 
        line = line
        type = type 
        var = var
    # TODO: about sub_stmt use to manage sub statment
    # for the program

class var(self): 
    u''' 
    '''
    def __init__(name, # Variable name must not be empty when initialize
                val=0, # Value for variable and must be INTEGER
    ): 
        name = name 
        val = val 
        init = 1 # if init # 0 -> cause runtime error 









