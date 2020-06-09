from ply import lex, yacc
print('Import lex and yacc successfully')


# List of tokens 
tokens = [
    "identifier",
    "number",
    "plus",
    "minus",
    "mult",
    "div"
]

# Tokens with regex rules
t_ignore = r" \t"
t_identifier = r"^[a-zA-Z]+$"
t_number = r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?"
t_plus = r"\+"
t_minus = r"-"
t_mult = r"\*"
t_div = r"/"
# TODO: ADD t_ignore_COMMENT


literals = ['+','-','*','/']

#-------------------------------PARSER---------------------------------- 

# Parser rules 
# expr : expr '+' term | expr '-' term | term
# term : term '*' factor | term '/' factor | factor
# factor : '(' expr ')' | identifier | number


# TODO: add p_list_stmt(p)



def p_stmt(p):
   """
      stmt : expr
   """
   p[0] = ("stmt", p[1])


# Consider to use precedence()
# to see if it can helps

def p_expr(p):
   """
      expr : expr plus term 
           | expr minus term 
           | term
   """
   p[0] = ("expr", p[1], p[2]) # Problem here <<<

def p_term(p):
   """
      term : term mult factor 
           | term div factor 
           | factor
   """

def p_factor(p):
   """
      factor : '(' expr ')' 
             | identifier 
             | number
   """


if __name__ == "__main__":
   lex.lex()
   yacc.yacc()
   data = "32 + 10"
   result = yacc.parse(data)
   print(result)

#TODO: Build AST


























































