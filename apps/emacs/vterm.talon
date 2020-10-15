user.vnc_app: emacs
win.title: /^Emacs;| Exceed/
#user.emacs_modes: /VTerm/
-
# - 

action(edit.delete_line): 
	key(ctrl-a)
	key(ctrl-k)
	
term go: "go\n"
term up <number>: user.term_up(number)
(cd | see dee) back: "cd -\n"
dir: "ls\n"
dir all: "la\n"

(cd | see dee) implementation: "cd impl\n"

find (path | pat): user.execute_command("vterm-insert-path")