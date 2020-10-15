app: outlook
-
tag(): user.tabs


view mail: key(ctrl+1)
view calendar: key(ctrl+2)
# - Search the mail in the current inbox
search mail: key(ctrl+e)

jump: 
    key(alt)

new mail: key(ctrl+shift+M)
reply: key(ctrl+r)
reply all: key(ctrl+shift+r)

mark unread: key(ctrl+u)
mark (read | red): key(ctrl+q)

#(pane|pain) next: key(ctrl-shift-tab)
#(pane|pain) next: key(shift-tab)
action(app.tab_next): 
    key(ctrl-shift-tab)
action(app.tab_previous):
    key(shift-tab)