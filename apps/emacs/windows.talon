# - Main file for all emacs related configuration
user.vnc_app: emacs
win.title: /^Emacs;| Exceed/
-

# - Window navigation
window up:
    key(ctrl-x ctrl-up)

window down:
    key(ctrl-x ctrl-down)

window left:
    key(ctrl-x ctrl-left)

window right:
    key(ctrl-x ctrl-right)

# - window jump
jump window:
    user.execute_command("window-number-switch")
