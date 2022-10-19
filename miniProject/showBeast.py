#!/usr/bin/python3
""" TLG Cohort D23 | CChea
    Text Based Adventure Game """
import introScene
import endScene

def main():
    direction = ["left", "right"]
    print("You hear the soft breakage of leaves and twigs nearby. Your adrenaline rises. Where would you like to go?")
    userInput = ""
    while userInput not in direction:
        print("Options: right, left, backward")
        userInput = input()
        if userInput == "right":
            introScene()
        elif userInput == "left":
            print("You find that vines magically grew to create a wall to stop you from going back. Your only option is to find another path forward")
        elif userInput == "backward":
            endScene()
        else:
            print("Please choose a valid option")

if __name__ == "__main__":
    main()
