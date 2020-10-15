from talon import Context, Module, actions, grammar, settings, fs
import os

# Add single words here if Talon recognizes them, but they need to have their
# capitalization adjusted.
capitalize = [
    "I",
    "I'm",
    "I've",
    "I'll",
    "I'd",
    "Monday",
    "Mondays",
    "Tuesday",
    "Tuesdays",
    "Wednesday",
    "Wednesdays",
    "Thursday",
    "Thursdays",
    "Friday",
    "Fridays",
    "Saturday",
    "Saturdays",
    "Sunday",
    "Sundays",
    "January",
    "February",
    # March omitted because it's a regular word too
    "April",
    # May omitted because it's a regular word too
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Add single words here if Talon recognizes them, but they need to have their
# spelling adjusted.
word_map = {
    # For example:
    # "color": "colour",
}


# Add words (or phrases you want treated as words) here if Talon doesn't
# recognize them at all.
#simple_vocabulary = ["nmap", "admin", "Cisco", "Citrix", "VPN", "DNS", "minecraft"]

# Add vocabulary words (or phrases you want treated as words) here that aren't
# recognized by Talon and are written differently than they're pronounced.
mapping_vocabulary = {
    # For example:
    # "enn map": "nmap",
    # "under documented": "under-documented",
}
#mapping_vocabulary.update(dict(zip(simple_vocabulary, simple_vocabulary)))
punctuation = set(".,-!?;:")



def parse_csv(files, delimiter):
    '''read in a csv file and return a dictionary with the from and to pairs'''
    d_pairs = {}
    # - make sure that the files list exists
    if files is not None and len(files):
        files = files.split(';')
        for file in files:
            print("Current file: " + str(file))
            with open(file, "r") as f:
                for pair in f:
                    pair = pair.rstrip()
                    pair = pair.split(delimiter)
                    #print("My pair " + str(pair))
                    # - if we have no mapped term, the -1
                    #   will grab the first term again period.
                    #   If there's a second colum mapping then we'll grab it too.
                    d_pairs[pair[0]] = pair[-1]
                    #print(str(d_pairs))
    return d_pairs
#cwd = os.path.dirname(os.path.realpath(__file__))
#my_file = os.path.join(cwd, "vocab_general.csv")
#parse_csv(my_file, "\t")
def on_change(path, exists):
    if path in registered_files:
        registered_files[path]("")
# - List of files that have been registered for watching of updates
registered_files = {}    
def register_files(files,cb):
    '''registered the file system to watch for updates in these files.'''
    global on_change
    if files is not None and len(files):
        files = files.split(';')
        for file in files:
            real_file = os.path.realpath(file)
            file_dir = os.path.dirname(real_file)
            if real_file not in registered_files:
                print("registering files: " + real_file)
                registered_files[real_file] = cb
                fs.watch(file_dir,on_change)
    
mod = Module()
mod.setting("vocabulary_csv_list", type="STRING", default="", desc="""a semicolon separated list of file paths pointed to csv files that will be used to add new words that are not recognized.""")
mod.setting("spelling_csv_list", type="STRING", default="", desc="""a semicolon separated list of file paths pointed to csv files that will be used to adjust spelling of recognized words. color->colour""")
#print("my setting" + str(settings.get("user.vocabulary_csv_list")))

mod.list("vocabulary", desc="user vocabulary")

ctx = Context()

def build_vocabulary(args):
    global mapping_vocabulary
    global word_map
    global capitalize
    print("Building vocabulary")
    # - Register a watcher on all the csv files
    files = settings.get("user.vocabulary_csv_list")
    mapping_vocabulary = parse_csv(files, ",")
    register_files(files,build_vocabulary)
    # user.vocabulary is used to explicitly add words/phrases that Talon doesn't
    # recognize. Words in user.vocabulary (or other lists and captures) are
    # "command-like" and their recognition is prioritized over ordinary words.
    ctx.lists["user.vocabulary"] = mapping_vocabulary


def build_spelling(args):
    global mapping_vocabulary
    global word_map
    global capitalize
    print("Building spelling")
    # - Register a watcher on all the csv files
    files = settings.get("user.spelling_csv_list")
    #mapping_vocabulary = parse_csv(settings.get("user.vocabulary_csv_list"), ",")
    word_map = parse_csv(files, ",")
    word_map.update({x.lower(): x for x in capitalize})
    
    # dictate.word_map is used by actions.dictate.replace_words to rewrite words
    # Talon recognized. Entries in word_map don't change the priority with which
    # Talon recognizes some words over others.
    ctx.settings["dictate.word_map"] = word_map

    # user.vocabulary is used to explicitly add words/phrases that Talon doesn't
    # recognize. Words in user.vocabulary (or other lists and captures) are
    # "command-like" and their recognition is prioritized over ordinary words.
    #ctx.lists["user.vocabulary"] = mapping_vocabulary

    

settings.register("post:user.vocabulary_csv_list", build_vocabulary)
settings.register("post:user.spelling_csv_list", build_spelling)
    
@mod.capture(rule="{user.vocabulary}")
def vocabulary(m) -> str:
    return m.vocabulary


@mod.capture(rule="(<user.vocabulary> | <word>)")
def word(m) -> str:
    try:
        return m.vocabulary
    except AttributeError:
        # TODO: if the word is both a regular word AND user.vocabulary, then in
        # principle it may parse as <word> instead; we ought to pass it through
        # mapping_vocabulary to be sure. But we should be doing that in
        # user.text, below, too.
        words = actions.dictate.replace_words(actions.dictate.parse_words(m.word))
        assert len(words) == 1
        return words[0]

@mod.capture(rule="(<user.vocabulary> | <phrase>)+")
def text(m) -> str:
    words = []
    for item in m:
        if isinstance(item, grammar.vm.Phrase):
            words.extend(
                actions.dictate.replace_words(actions.dictate.parse_words(item))
            )
        else:
            words.extend(item.split(" "))

    result = ""
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation and words[i - 1][-1] not in ("/-("):
            result += " "
        result += word
    return result


