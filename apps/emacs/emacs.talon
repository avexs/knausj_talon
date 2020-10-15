# - Main file for all emacs related configuration
user.vnc_app: emacs
win.title: /^Emacs;| Exceed/
-
cancel:
		key(ctrl-g)

new (term | terminal): 
	user.execute_command("vterm")

# - avy jump
#   jump to a character in the window
jump care:
    key("ctrl-u 1")
    user.execute_command("avy-goto-char")
#   jump to a character in any window
jump care all:
    user.execute_command("avy-goto-char")
#   jump to word start in the line
jump:
    user.execute_command("avy-goto-char-in-line")
jump word:
    user.execute_command("avy-goto-word-0-in-line")
jump word buffer:
    key("ctrl-u 1")
    user.execute_command("avy-goto-word-0")

# - Jump line.
spring <number>+:
    user.execute_command("goto-line")
    insert(number)
    key("enter")

# - Generic emacs controls
meta: 
    key(alt)
    
meta command:
    key(alt-x)
