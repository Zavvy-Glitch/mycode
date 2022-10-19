#!/usr/bin/python3
""" TLG Cohort D23 | CChea
    Text Based Adventure Game """
import introScene
import showBigCat

def main():
    direction = ["left", "right", "backward"]
    print("You hear the soft breakage of leaves and twigs nearby. You accidently anger a collective of wild boars. Your adrenaline rises. Where should you go?")
    userInput = ""
    while userInput not in direction:
        print("Options: right, left, backward")
        userInput = input()
        if userInput == "right":
            introScene.main()
        elif userInput == "left":
            print("Luckily, the boars are too frieghtened. You escaped with ease.")
            showBigCat.main()
        elif userInput == "backward":
            introScene.main()
        else:
            print("Please choose a valid option")

if __name__ == "__main__":
    main()
