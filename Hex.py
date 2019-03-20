class Hex:
    def __init__(self, name, resource, number):
        self.name = name
        self.resource = resource
        self.number = number
        self.settlements = [None] * 6
        self.roads = [None] * 6

    def __repr__(self):
        if self.name is 'Desert':
            return_str = self.name
            return return_str + ' ' * (10 - len(return_str))
        elif self.name is not 'None':
            return_str = self.resource + ": " + str(self.number)
            return return_str + ' ' * (10 - len(return_str))
        else:
            return ' '*10
