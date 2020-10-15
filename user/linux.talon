slap:
	edit.line_end()
	key(enter)
swat:
    edit.line_start()
    key(enter)
    key(up)
    
cd: "cd "
grep: "grep "
elle less: "ls "
(ls|el es|ellis|el less) : "ls "

(http | htp): "http"
(regex | rejex): "regex"
word queue: "queue"
word eye: "eye"
word iter: "iter"
word cmd: "cmd"
word dup: "dup"
word printf: "printf"
word shell: "shell"
zoom [in]: edit.zoom_in()
zoom out: edit.zoom_out()
(page | scroll) up: key(pgup)
(page | scroll) down: key(pgdown)
copy that: edit.copy()
cut that: edit.cut()
paste that: edit.paste()
paste match: edit.paste_match_style()
file save: edit.save()
#menu help: key(F1)
#spotlight: key(super)
undo that: edit.undo()
redo that: edit.redo()
volume up: key(volup)
volume down: key(voldown)
mute: key(mute)
play next: key(next)
play previous: key(prev)
(play | pause): key(play_pause)  
wipe: key(backspace)
(pad | padding): 
	insert("  ") 
	key(left)

