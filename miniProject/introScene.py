#!/usr/bin/python3
""" TLG Cohort D23 | CChea
    Text Based Adventure Game """

import showBigCat
import showBeast
import showVillage

def main():
    direction = ["left", "right", "forward", "backward"]
    print("You've found yourself at a 3 pronged path, again you can choose any direction you'd like to follow. Where would you like to proceed?")
    userInput = ""
    while userInput not in direction:
        print("Options: Left/Right/Backward/Forward")
        userInput = input()
        if userInput.lower() == "left":
            showBigCat.main()
        elif userInput.lower() == "right":
            showBeast.main()
        elif userInput.lower() == "backward":
            print("You find that vines magically grew to create a wall to stop you from going back. Your only option is to find another path forward")
            main()
        elif userInput.lower() == "forward":
            showVillage.main()
        else:
            print("Please choose a valid option")

if __name__ == "__main__":
    main()
