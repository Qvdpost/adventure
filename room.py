from collections import defaultdict

class Room:
    def __init__(self, uid, name, description):
        self._uid = uid
        self._name = name
        self._description = description
        self._connections = defaultdict(list)
        self._visited = False
        self._items = {}
    
    def add_connection(self, connection:'Connection'):
        self._connections[connection.direction].append(connection)

    def has_connection(self, direction):
        return direction in self._connections

    def get_connections(self, direction):
        return self._connections[direction]

    @property
    def is_forced(self):
        return 'FORCED' in self._connections

    def set_visited(self):
        self._visited = True

    def description(self, full=False):
        if not self._visited or self.is_forced or full is True:
            self.set_visited()
            return self._description + "\n" + "\n".join([item.__str__() for item in self._items.values()])

        return self._name

    def add_item(self, item):
        self._items[item.name] = item

    def has_item(self, item_name):
        return item_name in self._items

    def remove_item(self, item_name):
        return self._items.pop(item_name)

    def __str__(self):
        return f"Room {self._uid}"