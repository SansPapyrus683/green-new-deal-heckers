from dumbMazes.iHateMazes import findNeighbors
from collections import defaultdict

# this is the part 2 file

totalCoo = defaultdict(False)
generalStruct = set()
with open('redditGood.txt') as bugs:
    yVal = 0
    for line in bugs.readlines():
        xVal = 0
        for c in line.rstrip():
            generalStruct.add((xVal, yVal))  # we'll need the (2, 2) later- don't worry
            if xVal == 2 and yVal == 2:
                continue
            totalCoo[(xVal, yVal, 0)] = c == '#'
            xVal += 1
        yVal += 1

print(totalCoo)
print(generalStruct)


def erisNeighbors(cell: tuple):
    """each cell goes like (xValInCurrLevel, yValInCurrLevel, actualLevel(zCoo basically))
    it works w. the constraints in the problem, so it isn't general"""
    neighbors = {pt + (cell[-1],) for pt in findNeighbors(cell[:-1], generalStruct)}
    if (2, 2) in findNeighbors(cell[:-1], generalStruct):  # ok this one has 8, level goes +1
        neighbors.remove((2, 2, cell[-1]))
        if cell[:-1] == (2, 1):  # top
            neighbors.update({(n, 0, cell[-1] + 1) for n in range(5)})
        elif cell[:-1] == (3, 2):  # right
            neighbors.update({(4, n, cell[-1] + 1) for n in range(5)})
        elif cell[:-1] == (1, 2):  # left
            neighbors.update({(0, n, cell[-1] + 1) for n in range(5)})
        elif cell[:-1] == (2, 3):  # bottom
            neighbors.update({(n, 4, cell[-1] + 1) for n in range(5)})
    else:  # ok this one is one the outside, level goes -1
        if cell[0] == 0:  # all separate to account for corners
            neighbors.update({(1, 2, cell[-1] - 1)})
        if cell[0] == 5:
            neighbors.update({(3, 2, cell[-1] - 1)})
        if cell[1] == 0:
            neighbors.update({(2, 1, cell[-1] - 1)})
        if cell[1] == 5:
            neighbors.update({(2, 3, cell[-1] - 1)})
    return neighbors


for i in range(200):
    pass
