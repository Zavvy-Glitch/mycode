#!/usr/bin/python3
""" TLG Cohort D23 | CChea
    Text Based Adventure Game """

import introScene

if __name__ == "__main__":
    while True:
        print("Welcome to ___Adventure Game Name Goes Here ___")
        print("As an adept explorer, you decide you want to visit the Pyramids of Machu Picchu")
        print("During your path, you've found yourself lost in the jungles of Peru.")
        print("You can choose to walk in various directions to help you find your way to your final destination.")
        print("Lets start with your name, friend. What shall I call you? \n --->")

        name = input()
        print(f"Good luck, {name}. Be Weary of the Perils beyond!")
        introScene.main()
