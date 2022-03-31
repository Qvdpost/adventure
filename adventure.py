import loader

class Adventure():

    # Create rooms and items for the game that was specified at the command line
    def __init__(self, filename):
        self._current_room = loader.load_room_graph(filename)
        self._items = {}

    # Pass along the description of the current room, be it short or long
    def room_description(self):
        return self._current_room.description()

    def full_description(self):
        return self._current_room.description(full=True)

    def take(self, item_name):
        if self._current_room.has_item(item_name):
            self._items[item_name] = self._current_room.remove_item(item_name)
            return True
        return False
    
    def drop(self, item_name):
        if item_name in self._items:
            self._current_room.add_item(self._items.pop(item_name))
            return True
        return False

    # Move to a different room by changing "current" room, if possible
    def move(self, direction):
        if self._current_room.has_connection(direction):
            for connection in self._current_room.get_connections(direction):
                if connection.item is None or connection.item in self._items:
                    self._current_room = connection.destination
                    return True

        return False

    def is_forced(self):
        return self._current_room.is_forced

if __name__ == "__main__":

    from sys import argv

    # Check command line arguments
    if len(argv) not in [1,2]:
        print("Usage: python3 adventure.py [name]")
        exit(1)

    # Load the requested game or else Tiny
    print("Loading...")
    if len(argv) == 2:
        game_name = argv[1]
    elif len(argv) == 1:
        game_name = "Tiny"
    filename = f"data/{game_name}Adv.dat"

    # Create game
    adventure = Adventure(filename)

    # Welcome user
    print("Welcome to Adventure.\n")

    # Print very first room description
    print(adventure.room_description())

    # Prompt the user for commands until they type QUIT
    while True:

        # Prompt, converting all input to upper case
        command = input("> ").upper()

        # Perform the move or other command
        if adventure.move(command):
            print(adventure.room_description())
            while adventure.is_forced():
                adventure.move("FORCED")
                print(adventure.room_description())
        elif "TAKE" in command.split():
            if adventure.take(command.split()[1]):
                print("Item taken.")
            else:
                print("No such item.")
        elif "DROP" in command.split():
            if adventure.drop(command.split()[1]):
                print("Item dropped.")
            else:
                print("No such item.")
        elif command == "LOOK":
            print(adventure.full_description())
        # Allows player to exit the game loop
        elif command == "QUIT":
            break
        else:
            print("Invalid command.")
