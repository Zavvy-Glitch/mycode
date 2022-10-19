#!/usr/bin/python3
""" TLG Cohort D23 | CChea
    Text Based Adventure Game """

import introScene

def main():
    direction = ["left", "right", "backward", "forward"]
    print("You've managed to survive thus far, where to next?")
    userInput = ""
    while userInput not in direction:
        print("Options: right, left, backward, forward")
        userInput = input()
