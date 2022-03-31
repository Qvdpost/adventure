from room import Room
from connection import Connection
from item import Item

def load_room_graph(filename):
    rooms = {}
    with open(f"{filename}") as f:
        room_lines, connection_lines, item_lines = f.read().split("\n\n")
        
        for room_line in room_lines.split("\n"):
            room_info = room_line.split("\t")
            rooms[room_info[0]] = Room(*room_info)

        for connection_line in connection_lines.split("\n"):
            connection_info = connection_line.split("\t")
            source_room = rooms[connection_info[0]]
            for direction, destination in zip(*[iter(connection_info[1:])]*2):
                if "/" in destination:
                    destination, item = destination.split('/')
                    connection = Connection(direction, rooms[destination], item)
                else:
                    connection = Connection(direction, rooms[destination])
                source_room.add_connection(connection)

        for item_line in item_lines.strip("\n").split("\n"):
            item_info = item_line.split("\t")
            source_room = rooms[item_info[2]]
            source_room.add_item(Item(item_info[0], item_info[1]))
            
    return rooms['1']
            