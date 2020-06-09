
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "div identifier minus mult number plus\n      stmt : expr\n   \n      expr : expr plus term \n           | expr minus term \n           | term\n   \n      term : term mult factor \n           | term div factor \n           | factor\n   \n      factor : '(' expr ')' \n             | identifier \n             | number\n   "
    
_lr_action_items = {'(':([0,5,8,9,10,11,],[5,5,5,5,5,5,]),'identifier':([0,5,8,9,10,11,],[6,6,6,6,6,6,]),'number':([0,5,8,9,10,11,],[7,7,7,7,7,7,]),'$end':([1,2,3,4,6,7,13,14,15,16,17,],[0,-1,-4,-7,-9,-10,-2,-3,-5,-6,-8,]),'plus':([2,3,4,6,7,12,13,14,15,16,17,],[8,-4,-7,-9,-10,8,-2,-3,-5,-6,-8,]),'minus':([2,3,4,6,7,12,13,14,15,16,17,],[9,-4,-7,-9,-10,9,-2,-3,-5,-6,-8,]),')':([3,4,6,7,12,13,14,15,16,17,],[-4,-7,-9,-10,17,-2,-3,-5,-6,-8,]),'mult':([3,4,6,7,13,14,15,16,17,],[10,-7,-9,-10,10,10,-5,-6,-8,]),'div':([3,4,6,7,13,14,15,16,17,],[11,-7,-9,-10,11,11,-5,-6,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stmt':([0,],[1,]),'expr':([0,5,],[2,12,]),'term':([0,5,8,9,],[3,3,13,14,]),'factor':([0,5,8,9,10,11,],[4,4,4,4,15,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> stmt","S'",1,None,None,None),
  ('stmt -> expr','stmt',1,'p_stmt','parser.py',34),
  ('expr -> expr plus term','expr',3,'p_expr','parser.py',40),
  ('expr -> expr minus term','expr',3,'p_expr','parser.py',41),
  ('expr -> term','expr',1,'p_expr','parser.py',42),
  ('term -> term mult factor','term',3,'p_term','parser.py',48),
  ('term -> term div factor','term',3,'p_term','parser.py',49),
  ('term -> factor','term',1,'p_term','parser.py',50),
  ('factor -> ( expr )','factor',3,'p_factor','parser.py',55),
  ('factor -> identifier','factor',1,'p_factor','parser.py',56),
  ('factor -> number','factor',1,'p_factor','parser.py',57),
]
