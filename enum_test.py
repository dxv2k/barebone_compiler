from enum import Enum,auto

class statement_type(Enum):
    u'''
    '''

    incr_stmt = auto()
    decr_stmt = auto()
    while_stmt = auto()
    clear_stmt = auto()
    copy_stmt = auto()


class var(self):

    u'''
    '''

    def __init__(self, name, value = 0):
        self.name = name
        self.value = value

    def set_var(self, value):
        self.value = value

    def return_value(self):
        return self.value

    def return_name(self):
        return self.name

    def isInit(self, name_of_var):
        return 1

class stmt(self):
    u'''
    '''

    def __init__(self, type = None, line = None, var = None, var_destination = None, stmt_list = []):
        self.line = line
        self.type = type
        self.var = var
        #self.var_destination
        #self.stmt_list

    def return_line(self):
        return self.line


    def return_var_name(self):
        return self.var.name

    def return_var_value(self):
        return self.var.value

    #def add_stmt_to_list(stmt):
    #def getstmt_type

    def return_stmt_list(self):
        return self.stmt_list


