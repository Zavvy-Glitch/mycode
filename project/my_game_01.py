#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Implement simple game frameowrk with a dictionary object """


def showInstructions():
    """ Show Game Instructions When Invoked """
    print('''
    Your Objective - Reach the Garden! Oh, you'll also need to find Narsil 
        and a potion to win. GOOD LUCK!
    ==========================================================
          ''')

    print('''
    RPG GAME
    ========
    Commands:
        go [North, East, West, South]
        get [item] 
        ''')


def showStatus():
    """ Determines the current status of the player """

    print('-------------------------------------------')
    # Prints players inventory
    print('Inventory:', inventory)
    # Prints players current location
    print('Currently, you\'re in the ' + currentRoom)

    # Checks if there's an item in the current room, if item exists print
    if "item" in rooms[currentRoom]:
        print(f'You notice there\'s a {rooms[currentRoom]["item"]}')
    print('--------------------------------------------')


# variable to contain an empty list for inventory
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

currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()

    move = ''
    while move == '':
        move = input('> ')

    move = move.lower().split(" ", 1)

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(move[1] + ' obtained!')

            del rooms[currentRoom]['item']
        else:
            print('Can\'t get' + move[1] + '!')

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if 'narsil' in inventory:
            print('YOU LUCKED OUT! You have Narsil! YOU SLAY THE MONSTER!')
            del rooms[currentRoom]['item']
        else:
            print('A Monster has appeared! You\'re defenseless! You\'ve been mauled to death! GAME OVER!')
            break

    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('YOU ESCAPED! You were able to find the needed healing potion and Narsil(?) is that a win?')
        break
