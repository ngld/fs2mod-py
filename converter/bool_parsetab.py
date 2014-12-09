
# converter/bool_parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\x06\x19\xc9\x855\xd9S\xde\x8f\xd19\x13<\xffS\x85'
    
_lr_action_items = {'OR':([1,3,5,8,9,10,11,],[-5,7,-3,7,-1,-2,-4,]),'RPAREN':([1,5,8,9,10,11,],[-5,-3,11,-1,-2,-4,]),'ID':([0,2,4,6,7,],[1,1,1,1,1,]),'AND':([1,3,5,8,9,10,11,],[-5,6,-3,6,-1,-2,-4,]),'NEGATE':([0,2,4,6,7,],[2,2,2,2,2,]),'LPAREN':([0,2,4,6,7,],[4,4,4,4,4,]),'$end':([1,3,5,9,10,11,],[-5,0,-3,-1,-2,-4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,4,6,7,],[3,5,8,9,10,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression AND expression','expression',3,'p_expr_bin','converter/bool_parser.py',53),
  ('expression -> expression OR expression','expression',3,'p_expr_bin','converter/bool_parser.py',54),
  ('expression -> NEGATE expression','expression',2,'p_expr_neg','converter/bool_parser.py',60),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expr_parens','converter/bool_parser.py',65),
  ('expression -> ID','expression',1,'p_expr_id','converter/bool_parser.py',70),
]