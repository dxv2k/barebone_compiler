
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "0 CLEAR COPY DECR DO IDENT INCR INIT NOT NUMBER TO WHILE \n        stmt : clear_stmt\n     \n        init_stmt : INIT var '=' NUMBER ';'\n     \n        clear_stmt : CLEAR var ';'\n     \n        var : IDENT\n    "
    
_lr_action_items = {'CLEAR':([0,],[3,]),'$end':([1,2,6,],[0,-1,-3,]),'IDENT':([3,],[5,]),';':([4,5,],[6,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stmt':([0,],[1,]),'clear_stmt':([0,],[2,]),'var':([3,],[4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> stmt","S'",1,None,None,None),
  ('stmt -> clear_stmt','stmt',1,'p_stmt','bb_parser.py',58),
  ('init_stmt -> INIT var = NUMBER ;','init_stmt',5,'p_init_stmt','bb_parser.py',62),
  ('clear_stmt -> CLEAR var ;','clear_stmt',3,'p_clear_stmt','bb_parser.py',73),
  ('var -> IDENT','var',1,'p_var','bb_parser.py',81),
]
