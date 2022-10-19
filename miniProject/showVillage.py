#!/usr/bin/python3
""" TLG Cohort D23 | CChea
    Text Based Adventure Game """

import showBigCat
import showBeast
import introScene

def main():
    direction = ["left", "right", "forward", "backward"]
    print("You wound up at a village. Eerily, there isn't a soul in sight. There's a fire lit. You should keep moving. What direction do you want to go?")
    userInput = ""
    while userInput not in direction:
        print("Options: Left/Right/Backward/Forward")
        userInput = input()
        if userInput.lower() == "left":
            showBigCat.main()
        elif userInput.lower() == "right":
            showBeast.main()
        elif userInput.lower() == "backward":
            print("DEJA VU")
            main()
        elif userInput.lower() == "forward":
            introScene.main()
        else:
            print("Please choose a valid option")

if __name__ == "__main__":
    main()
