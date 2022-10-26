#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Practicing usng for loops to slice objects off of an API """

from random import randint
import requests
import wget

def main():
    """ ENTRY POINT """

    # will randomly generate a number between 1 && 905
    poke_num = str(randint(1, 905))

    # makes a request to the API and converts to pythonic data
    poke_api = requests.get("https://pokeapi.co/api/v2/pokemon/" + poke_num).json()
    print(f"{poke_api['name']} image- {poke_api['sprites']['front_default']}")
    # direct url path to poke sprites
    poke_img = poke_api["sprites"]["front_default"]

    # use wget to download image
    wget.download(poke_img, "/home/student/static/")
    # will iterate pokeapi pythonic data to find key of "moves" & then print the moves "name"
    for i in poke_api["moves"]:
        print(i["move"]["name"])
    # will count and print how many times this pokemon has appeared in one of their games
    games = 0
    print("These are the games this pokemon has appeared: ")
    for i in poke_api["game_indices"]:
        print(i)
        games += 1

    print("Total Games: ", games)

if __name__ == "__main__":
    main()
