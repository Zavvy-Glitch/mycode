#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Practice with try and except logic """

while True:
    try:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
    except:
        print("Error with that file name! Try again.")
