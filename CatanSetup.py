from Hex import Hex

import random

# Get the number of resource tiles and chits from a basic setup
resource_tuples = [('Field', 'Grain')] * 4 + [('Forest', 'Lumber')] * 4 + [('Pasture', 'Wool')] \
    + [('Mountain', 'Ore')] * 3 + [('Hill', 'Brick')] * 3
random.shuffle(resource_tuples)

chits = [2] + [12] + list(i for i in range(3, 12) if i != 7) * 2
chits_ordered = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

resource_hexes = []
for resource_tuple, chit in zip(resource_tuples, chits_ordered):
    resource_hexes.append(Hex(resource_tuple[0], resource_tuple[1], chit))

# Make the desert tile
desert_hex = Hex('Desert', 'None', 'None')
desert_index = random.randint(0, 19)
resource_hexes = resource_hexes[:desert_index] + [desert_hex] + resource_hexes[desert_index + 1:]


for hex_tile in resource_hexes:
    print(hex_tile)
