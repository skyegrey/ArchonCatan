class Hex:
    def __init__(self, name, resource, number):
        self.name = name
        self.resource = resource
        self.number = number
        self.settlements = [None] * 6
        self.roads = [None] * 6

    def __repr__(self):
        return "Hex: " + self.name + " Resource: " + self.resource + " Number: " + str(self.number)
