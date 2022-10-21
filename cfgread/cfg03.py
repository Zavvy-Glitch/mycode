#!/usr/bin/env python3

""" TLG Cohort D23 | CChea
    Practicing Reading Config Files """

lines = 0

files = input("Please type the file name you wish to open: \n --> ")

## create file object in "r"ead mode
with open(files, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    lines += 1
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(lines)
