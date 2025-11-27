#!/usr/bin/env python3
# adventure.py — Simple terminal adventure game (single file)
# Features:
# - Rooms with N/S/E/W exits
# - Items you can take/use
# - Inventory
# - A locked Treasure Room that requires a key

import sys

# Game map: each room has a description, exits, and items
MAP = {
    "Entrance": {
        "desc": "You stand before a small cottage. The door to the north is slightly ajar.",
        "exits": {"n": "Hall"},
        "items": []
    },
    "Hall": {
        "desc": "A cozy hall with portraits. Doors lead east, west, and south.",
        "exits": {"s": "Entrance", "e": "Kitchen", "w": "Locked Door"},
        "items": ["note"]
    },
    "Kitchen": {
        "desc": "A kitchen with a wooden table. There's a faint smell of spice.",
        "exits": {"w": "Hall"},
        "items": ["rusty key"]
    },
    "Locked Door": {
        "desc": "A heavy wooden door with iron bands. A small keyhole glints.",
        "exits": {"e": "Hall"},  # west would go to Treasure Room but it's locked initially
        "items": []
    },
    "Treasure Room": {
        "desc": "A glittering room full of chests. One chest sits on a pedestal.",
        "exits": {"w": "Locked Door"},
        "items": ["ancient treasure"]
    }
}

# Tracks whether the Locked Door is unlocked
GAME_STATE = {
    "unlocked_locked_door": False
}

# Player state
player = {
    "location": "Entrance",
    "inventory": []
}


def show_location():
    loc = player["location"]
    room = MAP[loc]
    print("\n=== {} ===".format(loc))
    print(room["desc"])
    if room["items"]:
        print("You see: " + ", ".join(room["items"]))
    exits = ", ".join(room["exits"].keys())
    print("Exits: " + exits)


def show_inventory():
    if player["inventory"]:
        print("Inventory: " + ", ".join(player["inventory"]))
    else:
        print("Inventory: empty")


def move(direction):
    loc = player["location"]
    room = MAP[loc]
    direction = direction.lower()
    if direction not in room["exits"]:
        print("You can't go that way.")
        return
    next_room = room["exits"][direction]

    # handle locked door behavior:
    if next_room == "Locked Door" and not GAME_STATE["unlocked_locked_door"]:
        # moving into Locked Door itself is allowed (it's a room). But moving from Locked Door west to Treasure Room is blocked.
        pass

    player["location"] = next_room
    # special: prevent entering Treasure Room unless unlocked
    if player["location"] == "Treasure Room" and not GAME_STATE["unlocked_locked_door"]:
        print("The door is locked. You need a key.")
        # move back to the Locked Door room
        player["location"] = "Locked Door"


def take(item_name):
    loc = player["location"]
    room = MAP[loc]
    items = room["items"]
    item_name = item_name.lower()
    for it in items:
        if it.lower() == item_name:
            player["inventory"].append(it)
            items.remove(it)
            print(f"You picked up the {it}.")
            return
    print("There's no {} here.".format(item_name))


def use(item_name):
    item_name = item_name.lower()
    if item_name not in [i.lower() for i in player["inventory"]]:
        print("You don't have that item.")
        return

    # Using the rusty key on the locked door unlocks the Treasure Room
    if item_name == "rusty key":
        # must be at the Locked Door to use it effectively
        if player["location"] == "Locked Door":
            if not GAME_STATE["unlocked_locked_door"]:
                GAME_STATE["unlocked_locked_door"] = True
                # add exit from Locked Door to Treasure Room
                MAP["Locked Door"]["exits"]["w"] = "Treasure Room"
                MAP["Treasure Room"]["exits"]["e"] = "Locked Door"
                print("You insert the rusty key into the lock. It turns! The Treasure Room is now open.")
            else:
                print("The door is already unlocked.")
        else:
            print("You try the key, but there's nothing to unlock here.")
    elif item_name == "note":
        print("The note reads: 'Seek the key where meals are cooked.'")
    else:
        print(f"You try to use the {item_name}, but nothing happens.")


def look():
    show_location()


def help_text():
    print("""
Commands:
  n/s/e/w         - move north/south/east/west
  look            - describe current location
  take <item>     - pick up an item
  use <item>      - use an item from your inventory
  inventory (i)   - show your inventory
  help (h)        - show this help
  quit (q)        - quit the game
Goal: find and take the ancient treasure in the Treasure Room.
""")


def check_win():
    if "ancient treasure" in [i.lower() for i in player["inventory"]]:
        print("\nYou hold the ancient treasure in your hands. You win! 🎉")
        return True
    return False


def process_command(cmd):
    parts = cmd.strip().split()
    if not parts:
        return False
    verb = parts[0].lower()

    if verb in ("n", "s", "e", "w"):
        move(verb)
    elif verb in ("look",):
        look()
    elif verb in ("take", "get"):
        if len(parts) < 2:
            print("Take what?")
        else:
            take(" ".join(parts[1:]))
    elif verb == "use":
        if len(parts) < 2:
            print("Use what?")
        else:
            use(" ".join(parts[1:]))
    elif verb in ("inventory", "i"):
        show_inventory()
    elif verb in ("help", "h"):
        help_text()
    elif verb in ("quit", "q", "exit"):
        print("Thanks for playing!")
        sys.exit(0)
    else:
        print("I don't understand that command. Type 'help' for commands.")
    return False


def main():
    print("Welcome to the Tiny Cottage Adventure!")
    print("Type 'help' for commands.\n")
    show_location()

    while True:
        cmd = input("\n> ")
        process_command(cmd)
        # show current location and inventory after each command (keeps it simple)
        show_location()
        # small hint: if you're at the Locked Door and it's locked, remind the player
        if player["location"] == "Locked Door" and not GAME_STATE["unlocked_locked_door"]:
            print("The locked door to the west needs a key.")
        if check_win():
            break


if __name__ == "__main__":
    main()
