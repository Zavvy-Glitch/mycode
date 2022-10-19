#!/usr/bin/python3
""" TLG Cohort D23 | CChea
    Text Based Adventure Game """

import introScene
import showVillage

def main():
    direction = ["left", "right", "forward", "backward"]
    print("You hear strange howling coming from amongst the surrounding forest. Where would you like to go?")
    userInput = ""
    while userInput not in direction:
        print("Options: Left/Right/Backward/Forward")
        userInput = input()
        if userInput.lower() == "left":
            print("You've found yourself amongst a clutter of ocelots. Overwhelmed by their numbers they've mauled you to death.")
            quit()
        elif userInput.lower() == "right":
            introScene.main()
        elif userInput.lower() == "backward":
            print("You found your way out! Congrats you've found the pyraminds!")
            quit()
        elif userInput.lower() == "forward":
            showVillage.main()
        else:
            print("Please choose a valid option")

if __name__ == "__main__":
    main()
