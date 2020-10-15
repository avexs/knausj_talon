# - The below code will print the window title to the log when you 
#   switch windows. You can maitain a dictionary of terms that 
#   can be returned from this funciton which are then ascessible from the user.* key.
from talon import ctrl, ui, Module, Context, actions, clip, app
import re
mod = Module()
ctx = Context()

@mod.scope
def scope():
    win = ui.active_window()
    #print(win.title)
    #results = re.search ('^Emacs; Path=(.*)', win.title)
    #results = re.search ('^Emacs', win.title)

    #attrs = vars(ctx)
    #print(', '.join("%s: %s" % item for item in attrs.items()))
    #print(attrs.keys())
    
    vnc_app = "Unknown"
    emacs_path = ""
    emacs_modes = ""
    if re.match('^Emacs', win.title) is not None:
        vnc_app = "emacs"
        results = re.search ('Modes=\((.*)\)', win.title)
        if results is not None:
            #emacs_path = results.groups(1)
            emacs_modes = str(results.groups(1))
    #print(etx_app)
    #print(emacs_modes)
    return_dict = {}
    #return_dict['vnc_app'] = vnc_app
    print("hacking vnc_app")
    return_dict['vnc_app'] = "emacs"
    return_dict['emacs_modes'] = emacs_modes
    return_dict['emacs_path'] = emacs_path
    return return_dict
        
ui.register('win_title', scope.update)



@mod.action_class
class Actions:
    def term_up(number: int):
        """insert up<num> into terminals. This maps to an alias to cd ../ and the number of directories up matches the number"""
        if number == 1:
            actions.insert("up")
        else:
            actions.insert("up"+str(number))
                
        actions.key("enter")

    def execute_command(command: str):
        '''execute a command in emacs without opening the completion window'''
        actions.key("ctrl-c x")
        actions.insert(command)
        actions.key("enter")
