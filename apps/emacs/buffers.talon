# - buffer control configuration  
user.vnc_app: emacs
win.title: /^Emacs;| Exceed/
-

switch buffer:
	key(ctrl-x)
	key(b)

action(app.tab_previous):
    key(ctrl-x left)
    
action(app.tab_next):
    key(ctrl-x right)

	
kill buffer:
	key(ctrl-x)
	key(k)

action(app.tab_close):
    key(ctrl-x)
	key(k)
    key(enter)
kill buffer now: app.tab_close()
	
file open:
	key(ctrl-x)
	key(ctrl-f)

file open other:
	key(ctrl-x)
	key(4)
	key(f)
		
focus mini:
	key(ctrl-c)
	key(o)