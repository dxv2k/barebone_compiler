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

class stmt(): 
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
        self.stmt_t = type 
        self.var = var
        self.stmt_list = stmt_list

    # TODO: add try_catch/raise exception 
    def getLine(self): 
        return self.line
    def getType(self): 
        return self.stmt_t
    def getVar(self): 
        return self.var
    def get_stmt_list(self): 
        return stmt_list


class var(): 
    u''' 
    '''
    def __init__(self,
                name, # Variable name must not be empty when initialize
                value=0, # Value for variable and must be INTEGER
    ): 
        self.name = name 
        self.value = value 
        # self.init = 1
        # TODO: add try_catch/raise exception 

    def setValue(self,new_value): 
        self.value = new_value 

    def getName(self): 
        return self.name

    def getValue(self): 
        return self.value


# List for whole program
list_var_prog = [] # Contains list of variable that used in program 
list_stmt_prog = [] # Contains list of statement that used in program

def add_stmt_to_list(list, stmt): 
    u''' 
        list : expected to receive list object 
        stmt : expected to receive stmt from stmt() class 
    ''' 
    list.append(stmt)

def set_var(var_name,var_value=0): 
    list_var_prog.append(var(var_name,var_value)) 

def find_var(var_name): 
    u''' 
        find_var() expected to receive variable from var() class
    '''
    for var in list_var_prog: 
        if var.getName() == var_name: 
            return var
    # If var is not initialed yet then find_var will init
    # by itself 
    set_var(var_name)

def execute_stmt(stmt): 
    return 0 

def execute_stmt_list(stmt_list): 
    return 0 







