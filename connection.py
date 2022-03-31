class Connection:
    def __init__(self, direction, destination, item=None):
        self.direction = direction
        self.destination = destination
        self.item = item

    def __repr__(self):
        return f"{self.direction}: {self.destination}" 