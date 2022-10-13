#!/usr/bin/env python3

# the choice() function from the random module
# will choose a random element from a list
from random import choice

wordbank= ["indentation", "spaces"]

tlgstudents= ["Cat", "Chris", "Dao", "David", "Henwin", "Herman", "Jose", "Justin", "Kris", "Mannie", "Marcos", "Marshall", "Michael", "Mike", "Nikko", "Phil", "Ryan", "Sachin", "Samekh", "Will"]

# this will add the integer 4 to the wordbank list
wordbank.append(4)

# using """three quotes""" creates a multi-line doc string
# in other words, a string that uses line breaks instead of /n
print("""Do one of the following:
        - Enter a number between 0 and 17
        - Type in a student's name
        - Type in the word 'random'""")

# save the user's input as the variable "choice"
selection = input(">")

# if the number entered by the user can be
# cleanly converted to an integer:
if selection.isdigit():
    # convert string to integer and slice the list
    # save the returned name as "name"
    name = tlgstudents[int(selection)]

# if the name chosen is actually in the list of students:
elif selection in tlgstudents:
    # assign that name as the variable "name"
    name = selection

else:
    # if none of the above is true, use the choice()
    # function to grab a random name and save it as "name"
    name = choice(tlgstudents)

# Use an f-string to neatly combine these elements into a sentence.
print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")


