#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Working on slicing dictionaries """

def mainChallenge():

    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

    a = challenge[2][1]
    b = challenge[2][0]
    c = challenge[3]

    print(f"My {a}! The {b} do {c}!")

mainChallenge()

def mainTrial():

    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
        
    a = trial[2]["goggles"]
    b = trial[2]["eyes"]
    c = trial[3]

    print(f"My {a}! The {b} do {c}!")

mainTrial()

def mainNightmare():

    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

    a = nightmare[0]["user"]["name"]["first"]
    b = nightmare[0]["kumquat"]
    c = nightmare[0]["d"]

    print(f"My {a}! The {b} do {c}!")

mainNightmare()

