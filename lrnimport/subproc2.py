#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Scripting Commands Practice"""

import subprocess

subprocess.call(["ip", "link", "show", "up"])
print("This program will check your interfaces")
interface = input("Enter an interface, ie. ens3: \n ---> ")
subprocess.call(["ip", "addr", "show", "dev", interface])
subprocess.call(["ip", "route", "show", "dev", interface])
