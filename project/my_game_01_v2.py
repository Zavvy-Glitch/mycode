#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Implement simple game frameowrk with a dictionary object """

import requests
from random import randint


def monster():
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(randint(1, 151))).json()
    print(pokeapi["sprites"]["front_default"])


def show_instructions():
    """ Show Game Instructions When Invoked """
    print('''
    Your Objective - Reach the Garden!
    Oh, you'll also need to find Narsil and a potion to win. 
    GOOD LUCK!
    ==========================================================
          ''')

    print('''
    RPG GAME
    ========
    Commands:
        go [North, East, West, South]
        get [item] 
        ''')


def show_status():
    """ Determines the current status of the player """

    print('-------------------------------------------')
    # Prints players inventory
    print('Inventory:', inventory)
    # Prints players current location
    print('Currently, you\'re in the ' + current_room)

    # Checks if there's an item in the current room, if item exists print
    if "item" in rooms[current_room]:
        print(f'You notice there\'s a {rooms[current_room]["item"]}')
    print('--------------------------------------------')


# variable to contain an emty list for inventory
inventory = []

# variable to contain a dictionary of interconnected rooms
rooms = {
    'Hall': {
        'south': 'Kitchen'
    },
    'Kitchen': {
        'north': 'Hall',
        'east': 'Parlor',
        'west': 'Dining Room',
        'south': 'Garage',
        'item': 'key'
    },
    'Parlor': {
        'west': 'Kitchen',
        'north': 'Dining Room',
        'east': 'Garage',
        'item': 'monster'
    },
    'Dining Room': {
        'south': 'Parlor',
        'east': 'Kitchen',
        'north': 'Garden',
        'item': 'potion'
    },
    'Garage': {
        'north': 'Kitchen',
        'west': 'Parlor',
        'item': 'narsil'
    },
    'Garden': {
        'south': 'Dining Room'
    }
}

current_room = 'Hall'

show_instructions()

while True:
    show_status()

    move_choice = ''
    while move_choice == '':
        move_choice = input('> ')

    move_choice = move_choice.lower().split(" ", 1)

    if move_choice[0] == 'go':
        if move_choice[1] in rooms[current_room]:
            current_room = rooms[current_room][move_choice[1]]
        else:
            print('You can\'t go that way!')
    if move_choice[0] == 'get':
        if "item" in rooms[current_room] and move_choice[1] in rooms[current_room]['item']:
            inventory.append(move_choice[1])
            print(move_choice[1] + ' obtained!')

            del rooms[current_room]['item']
        else:
            print('Can\'t get' + move_choice[1] + '!')
    if 'item' in rooms[current_room] and 'monster' in rooms[current_room]['item']:
        if 'narsil' in inventory:
            monster()
            print('YOU LUCKED OUT! You have Narsil! YOU SLAY THE MONSTER!')
            del rooms[current_room]['item']
        else:
            monster()
            print('''
            A Monster has appeared! 
            You\'re defenseless! 
            You\'ve been mauled to death! 
            GAME OVER!!!!
            ''')
            break
    if current_room == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('''
        YOU ESCAPED! 
        You were able to find the needed healing potion and Narsil(?) 
        Is that a win?
        ''')
        break
