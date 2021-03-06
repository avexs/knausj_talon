find it:
    edit.find()

next one:
    edit.find_next()

go word left:
    edit.word_left()

go word right:
    edit.word_right()

go (lef|left):
    edit.left()

go (wry|right):
    edit.right()

go upper:
    edit.up()

go down:
    edit.down()

go line start:
    edit.line_start()

go line end:
    edit.line_end()

go way left:
    edit.line_start()
    edit.line_start()

go way right:
    edit.line_end()

go way down:
    edit.file_end()

go way upper:
    edit.file_start()

go page down:
    edit.page_down()

go page upper:
    edit.page_up()

# selecting
select line:
    edit.line_start()
    edit.extend_line_end()

select all:
    edit.select_all()


select left:
    edit.extend_left()

select right:
    edit.extend_right()

select upper:
    edit.extend_line_up()

select down:
    edit.extend_line_down()

select word left:
    edit.extend_word_left()

select word right:
    edit.extend_word_right()

select way left:
    edit.extend_line_start()

select way right:
    edit.extend_line_end()

select way upper:
    edit.extend_file_start()

select way down:
    edit.extend_file_end()

# editing
indent [more]:
    edit.indent_more()

(indent less | out dent):
    edit.indent_less()

# deleting
kill line:
    edit.delete_line()

kill upper:
    edit.extend_line_up()
    edit.delete()

kill down:
    edit.extend_line_down()
    edit.delete()

kill (lef|left):
    edit.extend_word_left()
    edit.delete()

kill (wry|right):
    edit.extend_word_right()
    edit.delete()

kill way left:
    edit.extend_line_start()
    edit.delete()

kill way right:
    edit.extend_line_end()
    edit.delete()

kill way upper:
    edit.extend_file_start()
    edit.delete()

kill way down:
    edit.extend_file_end()
    edit.delete()

#copy commands
copy all: 
    edit.select_all()
    edit.copy()
#to do: do we want these variants, seem to conflict
# copy left: 
#      edit.extend_left()
#      edit.copy()
# copy right: 
#     edit.extend_right()
#     edit.copy()
# copy upper: 
#     edit.extend_up()
#     edit.copy()
# copy down: 
#     edit.extend_down()
#     edit.copy()
copy word left: 
    edit.extend_word_left()
    edit.copy()
copy word right: 
    edit.extend_word_right()
    edit.copy()
#cut commands
cut everything: 
    edit.select_all()
    edit.cut()
#to do: do we want these variants
# cut left: 
#      edit.select_all()
#      edit.cut()
# cut right: 
#      edit.select_all()
#      edit.cut()
# cut upper: 
#      edit.select_all()
#     edit.cut()
# cut down: 
#     edit.select_all()
#     edit.cut()
cut word left: 
    edit.extend_word_left()
    edit.cut()
cut word right: 
    edit.extend_word_right()
    edit.cut()
