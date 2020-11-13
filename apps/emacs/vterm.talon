user.vnc_app: emacs
win.title: /^Emacs;| Exceed/
user.emacs_modes: /VTerm/
-
# - 

action(edit.delete_line): 
	key(ctrl-a)
	key(ctrl-k)
	
term go: "go\n"
term up <number>: user.term_up(number)
term back: "cd -\n"
(cd | see dee): "cd "
grep: "grep "
elle less: "ls "
(ls|el es|ellis|el less) : "ls "

dir: "ls\n"
dir all: "la\n"

(cd | see dee) implementation: "cd impl\n"

find (path | pat): user.execute_command("vterm-insert-path")


# - word select
action(edit.word_left):
	key(alt-b)

action(edit.word_right):
	key(alt-f)

kill (lef|left):
    key(alt-delete)

kill (wry|right):
    key(alt-d)
    