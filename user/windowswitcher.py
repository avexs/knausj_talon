from talon import Context, Module, app, clip, cron, imgui, actions, ui
from ...knausj_talon.code.keys import default_alphabet, letters_string
import win32gui
import win32con
from subprocess import run
from math import log, ceil

ctx = Context()

mod = Module()
mod.list('window_selection_words', desc='list of words ')
mod.list('homophones_selections', desc='list of valid selection indexes')

@mod.capture
def window_selection_words(m) -> int:
    "Returns the index of the aplication selected via letter words"

shown_windows = []
# window_codes = []
window_spelling = []

# - windows returned by win32.
#   this contains the list of window a handless that will be used to make the list.
valid_wins = []

@imgui.open(y=0,software=True)
def gui(gui: imgui.GUI):
    global shown_windows
    global window_spelling
    global groups
    global valid_wins
    gui.text("Select a window")
    index = 0
    gui.line()
    gui.text("desktop {0}")
    col_width = max(len(word) for word in window_spelling) + 2
    #print("Col width: " + str(col_width))
    #print(ctx.settings["imgui.font"])
    for win in groups:
        #print("width: " + str(len(window_spelling[index].ljust(col_width))))
        if gui.button("switch {} || {}".format(window_spelling[index].ljust(col_width), win32gui.GetWindowText(win))):
            switch_to_window_focus(win)
            actions.user.close_window_switcher()
        index = index + 1

    gui.line()
    if gui.button("close"):
        actions.user.close_window_switcher()


def make_combinations(amount):
    base_pieces = len(default_alphabet)
    base_num = ceil(log(amount, base_pieces))

    pieces = [0] * base_num
    results = []
    while len(results) < amount:
        for pos in range(base_num - 1, -1, -1):
            pieces[pos] += 1
            if pieces[pos] == base_pieces:
                pieces[pos] = 0
            else:
                break
        want_skip = False
        for i in range(0, len(pieces) - 1):
            if pieces[i] == pieces[i + 1]:
                want_skip = True
        if not want_skip:
            results.append(list(pieces))

    return results

def switch_to_window_focus(window: int):
    """responsible for maximizing or restoring windows when selected"""
    #win32gui.ShowWindow(window, win32con.SW_RESTORE)
    #win32gui.BringWindowToTop(window)
    # - check if the window is minimized in the tray.
    #   if so then we need to restore the window
    if (win32gui.IsIconic(window)):
        win32gui.ShowWindow(window, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(window)
    

def build_valid_wins( hwnd, ctx ):
    if (win32gui.IsWindowVisible( hwnd ) and len(win32gui.GetWindowText( hwnd )) > 0):
        valid_wins.append(hwnd)
    
@mod.action_class
class Actions:
    def show_window_switcher():
        """Display a window switcher"""
        global shown_windows
        global window_spelling
        global groups
        global valid_wins

        #shown_windows = ui.windows()
        #print(shown_windows)
        # wmctrl -l gives us window IDs (in hex) and desktop numbers (-1 is pinned)
        #desk_map = run(["wmctrl", "-l"], capture_output=True, encoding="utf8").stdout.splitlines()
        valid_wins.clear()
        # https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
        # - We will have enumareted all the windows.
        win32gui.EnumWindows( build_valid_wins, None )
        # - Sort the the windows, so that the combinations are more predictablels 
        valid_wins = sorted(valid_wins, key=win32gui.GetWindowText)
        
        combs = make_combinations(len(valid_wins))

        # grab the desktops that have windows
        #groups = sorted(set(desk_map.values()))
        #print("hello" + str(groups))

        # put a list of all window objects that are on one desktop for each desk
        #groups = { k: list(filter(lambda e: desk_map[e.id] == k, shown_windows)) for k in groups }
        shown_windows = []

        # make a flat list
        #for k in groups:
        #    shown_windows.extend(groups[k])
        groups = valid_wins
        # turn letter combos into word combos (ab -> air bat)
        window_spelling = list(map(lambda entry: " ".join(map(lambda digit: default_alphabet[digit], entry)), combs))
        ctx.lists['self.window_selection_words'] = window_spelling

        gui.show()

    def switch_to_window(window: int):
        """Switch to the window at the given index"""
        global shown_windows
        # global window_codes
        global window_spelling
        switch_to_window_focus(window)
        gui.hide()
        shown_windows = []
        # window_codes = []
        window_spelling = []
       
        
    def close_window_switcher():
        """Close the window switcher gui"""
        global shown_windows
        global window_spelling
        global groups
        global valid_wins    
        gui.hide()
        shown_windows = []
        window_spelling = []
        groups = []
        valid_wins = []

@ctx.capture(rule='{self.window_selection_words}')
def window_selection_words(m):
    #print(m.window_selection_words)
    taken = window_spelling.index(m.window_selection_words)
    print(groups[taken])
    #return groups.index(m.window_selection_words)
    return groups[taken]

ctx.lists['self.window_selection_words'] = []
