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
    # add_clear_stmt = auto() # TODO: This one not sure 

class stmt(self): 
    u'''
    '''
    def __init__(self,
                current_line=None, # use for tracking statement line in 
                                   # whole program
                type=None, # stmt_type(Enum) passthrough here  
                var=None, # variable name 
                var_dest=None, # Use for copy_stmt only 
                stmt_list=[] # Use for while_loop() only 
                             # Variable that init in stmt_list will be discarded
                             # after while_loop() completed
    ): 
        self.line = current_line
        self.type = type 
        self.var = var
    # TODO: add try_catch/raise exception 
    # def return_line(self): 
    #     return self.line

class var(self): 
    u''' 
    '''
    def __init__(self,
                name, # Variable name must not be empty when initialize
                value=0, # Value for variable and must be INTEGER
    ): 
        self.name = name 
        self.value = value 
        # TODO: add try_catch/raise exception 

    def set_var(self,new_value): 
        self.value = new_value 

    def return_name(self): 
        return self.name

    def return_val(self): 
        return self.value

def find_var(var_name): 
    u''' 
        find_var() expected to receive variable from var() class
    '''
