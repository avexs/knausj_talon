from talon import actions, Module, speech_system, ui, clip, imgui, Context
from ...knausj_talon.code.keys import default_alphabet, letters_string
from math import log, ceil
mod = Module()
ctx = Context()
mod.list('hinting_gui_combinations', desc='list of letter combinations making up the gui letter matching')
ctx.lists['self.hinting_gui_combinations'] = []
jump_data = []
current_line = ""
current_application = None
@imgui.open(y=0,software=False)
def gui(gui: imgui.GUI):
    global jump_data
    global current_line
    gui.text("Select a word")
    index = 0
    gui.line()

    for combo,word,index in jump_data:
        if gui.button("{} || {}".format(combo,word)):
            gui.hide()
            actions.sleep("10ms")
            current_application.focus()
            actions.user.jump_word_start(word,current_line)
    
    gui.line()
    if gui.button("close"):
        gui.hide()

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
        

def get_current_line():
    '''capture the current line and return it as a string'''
    actions.edit.line_end()
    actions.edit.select_line()
    line = actions.edit.selected_text()
    actions.edit.line_end()
    return line


def calculate_cursor_move_in_line(word: str, line: str):
   '''Calculate the number of cursor moves to position the cursor 
      at the beginning of the selected word in the string.
      assumes that the cursor is at the end of the line.'''
   if len(line):
       # - only split the words based upon spaces, we can ignore punctuation.
       list_line = line.split(" ")
       try:
           index_line = list_line.index(word)
           # - calculate the number of characters we need to move left
           number_spaces  = len(list_line) - index_line
           additional_characters = 0
           for x in list_line[index_line+1:]:
               additional_characters += len(x)
               #print("the number of additional characters: " + str(additional_characters))
           return additional_characters + number_spaces + len(word) - 1
       except ValueError:
           print("probably couldn't find that the word inside of the line provided")
           return -1
   else:
       return -1


@mod.action_class
class Actions:
    def jump_gui_select(m):
        '''temporary holder'''
        
    def jump_word_start(word: str, line: str = None):
        """Replace a word in the last string"""
        if line is None:
            line = get_current_line()
        number_moves = calculate_cursor_move_in_line(word,line)
        for _ in range(number_moves):
            actions.key("left")

    def jump_gui_word_start():
        '''Jump to the word start when using the gui to select the wordt'''
        global jump_data
        global current_line
        global current_application
        current_application = ui.active_app()
        line = get_current_line()
        current_line = line
        list_line = line.split(" ")
        combinations = make_combinations(len(list_line))
        alphabet_combinations = list(map(lambda entry: " ".join(map(lambda digit: letters_string[digit], entry)), combinations))
        print(str(alphabet_combinations))
        data = list(zip(alphabet_combinations, list_line, range(len(list_line))))
        print(str(data))
        #ctx.lists['self.hinting_gui_combinations'] = data
        jump_data = data
        gui.show()
        
        
        


 
 
@ctx.capture(rule='{self.hinting_gui_combinations}')
def hinting_selection_words(m):
    #print(m.window_selection_words)
    #taken = .index(m.window_selection_words)
    print(groups[taken])
    #return groups.index(m.window_selection_words)
    return groups[taken]

ctx.lists['self.window_selection_words'] = []
