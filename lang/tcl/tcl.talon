mode: user.tcl
-
tag(): user.code_operators
tag(): user.code_comment
tag(): user.code_generic
tickle: "tcl"
args: 
	insert("{}")
	key(left)
[inside] (index | array): 
	insert("[]") 
	key(left)
list in it: 
	insert("[]") 
	key(left)
(block | lock): 
	insert("{}") 
	key(left enter enter up tab)

if: "if "	

puts: "puts "

get (db|dee bee): "get_db "
set (db|dee bee): "set_db "

quotes: 
	insert("\"\"")
	key(left)
#   code block
action(user.code_block):
    insert("{\n\n}")
    key(up)

#   operators
action(user.code_operator_indirection): ""
action(user.code_operator_address_of): ""
action(user.code_operator_structure_dereference): ""
action(user.code_operator_lambda): ""
action(user.code_operator_subscript):
    insert("[]")
    key(left)
action(user.code_operator_assignment):
    insert("set ")
action(user.code_operator_subtraction): " - "
action(user.code_operator_subtraction_assignment): ""
action(user.code_operator_addition): " + "
action(user.code_operator_addition_assignment): ""
action(user.code_operator_multiplication): " * "
action(user.code_operator_multiplication_assignment): ""
action(user.code_operator_exponent): " ** "
action(user.code_operator_division): " / "
action(user.code_operator_division_assignment): ""
action(user.code_operator_modulo): " % "
action(user.code_operator_modulo_assignment): ""
action(user.code_operator_equal): " == "
action(user.code_operator_not_equal): " != "
action(user.code_operator_greater_than): " > "
action(user.code_operator_greater_than_or_equal_to): " >= "
action(user.code_operator_less_than): " < "
action(user.code_operator_less_than_or_equal_to): " <= "
action(user.code_operator_and): " && "
action(user.code_operator_or): " || "
action(user.code_operator_bitwise_and): " & "
action(user.code_operator_bitwise_and_assignment): ""
action(user.code_operator_bitwise_or): " | "
action(user.code_operator_bitwise_or_assignment): ""
action(user.code_operator_bitwise_exclusive_or): " ^ "
action(user.code_operator_bitwise_exclusive_or_assignment): ""
action(user.code_operator_bitwise_left_shift): ""
action(user.code_operator_bitwise_left_shift_assignment): ""
action(user.code_operator_bitwise_right_shift): ""
action(user.code_operator_bitwise_right_shift_assignment): ""

#   structures
action(user.code_state_if):
    insert("if {}")
    key(left)
action(user.code_state_else_if):
    key(end)
    insert(" elseif {}")
    key(left)
action(user.code_state_else):
    key(end)
    insert(" else ")
    user.code_block()
action(user.code_state_switch): ""
action(user.code_state_case): ""
action(user.code_state_for): "for "
action(user.code_state_for_each):
    insert("for in ")
    key(left)
    edit.word_left()
    key(space)
    edit.left()
action(user.code_state_while):
    insert("while :")
    edit.left()
action(user.code_type_class): "class "
action(user.code_import): "import "
action(user.code_from_import):
    insert("from import ")
    key(left)
    edit.word_left()
    key(space)
    edit.left()
action(user.code_comment): "# "
action(user.code_state_return):
	insert("return ")
action(user.code_true): "True"
action(user.code_false): "False"


#  Additional tcl commands
op assign wrap:
   edit.line_end()
   insert("]")
   edit.line_start()
   user.code_operator_assignment()
   insert(" ")
   insert("[")
   key(left)
   key(left)
  
   