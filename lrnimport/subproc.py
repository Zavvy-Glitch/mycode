#!/usr/bin/python3

""" TLG Cohort D23 | CChea 
    Practice scripting commands """

from subprocess import call

call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")

interface = input("Enter an interface, i.e. ens3: \n --> ")

call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])
