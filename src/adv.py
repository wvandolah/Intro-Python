# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.

# These are the existing rooms. Add more as you see fit.
import textwrap



rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
        "items": ["sword", "ring", "bow"]
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
        "items": ["stick", "shirt", "bow"]
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s_to": "narrow",
        "items": ["alian head"]
    },

}

""" template room to copy into code
    "room": {
        "name": "",
        "description": "",
        "n_to": "",
        "s_to": "",
        "e_to": "",
        "w_to": "",
    },
"""

# Write a class to hold player information, e.g. what room they are in currently

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

class Player:
    def __init__(self, setRoom, setItems):
        self.currentRoom = setRoom
        self.playerItems = setItems



def movingRooms(theD):
    if theD in rooms[newPlayer.currentRoom]:
        # print("fuck yes")
        newPlayer.currentRoom = rooms[newPlayer.currentRoom][theD]
    else:
        print("\nYou can't go that way!!!!  Learn to read!!!!!\n")

def grabItem(theI):
    if theI in rooms[newPlayer.currentRoom]['items']:
        newPlayer.playerItems.append(theI)
        rooms[newPlayer.currentRoom]['items'].remove(theI)
        print('found it!', newPlayer.playerItems)
    elif theI == "n":
        print("So you're too good for these items? A very bold move!")
    else:
        print("that wasn't an item, better luck next time")


newPlayer = Player("outside", [])

playing = True

while playing:
    print("\n########################\n\n{}\n".format(rooms[newPlayer.currentRoom]['name']))

    for l in textwrap.wrap(rooms[newPlayer.currentRoom]['description'],width=50):
        print("{}".format(l))
    
    

    print("\nItems found in room:")
    if "items" in rooms[newPlayer.currentRoom]:
        for index, item in enumerate(rooms[newPlayer.currentRoom]['items'], start=1):
            print("{}: {}".format(index,item))
        if not rooms[newPlayer.currentRoom]["items"]:
            print("none") 
    else:
        print("none")
    print("\n")

    userControl = input("what do you want to do? \ni=Check inventory, g=grab and item, n=north, s=south, e=east, w=west, q=quit: ")

    if userControl == "q":
        playing = False
    elif userControl in ['e','s','n','w']:
        # print('found control')
        movingRooms("{}_to".format(userControl))
        # newPlayer.currentRoom = rooms[newPlayer.currentRoom]["{}_to".format(userControl)]
    elif userControl == "i":
        print("########## You are holding:")
        for i in newPlayer.playerItems:
            print(i)
        print("##########")
    elif userControl == "g":
        itemControl = input("\nType name of item to pick up, or type \"n\": ")
        grabItem(itemControl)
    else:
        print("########################\n{} is not something this game is able to do. try again".format(userControl))
