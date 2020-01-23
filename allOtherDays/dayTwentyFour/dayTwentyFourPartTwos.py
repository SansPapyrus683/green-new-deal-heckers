from dumbMazes.iHateMazes import findNeighbors
from sys import exit

# this is the part 2 file

totalCoo = {}
generalStruct = set()
with open('redditGood.txt') as bugs:
    yVal = 0
    for line in bugs.readlines():
        xVal = 0
        for c in line.rstrip():
            generalStruct.add((xVal, yVal))  # we'll need the (2, 2) later- don't worry
            if xVal == 2 and yVal == 2:
                xVal += 1
                continue
            totalCoo[(xVal, yVal, 0)] = c == '#'
            xVal += 1
        yVal += 1


def erisNeighbors(cell: tuple):
    """each cell goes like (xValInCurrLevel, yValInCurrLevel, actualLevel(zCoo basically))
    it works w. the constraints in the problem, so it isn't general"""
    neighbors = {point + (cell[-1],) for point in findNeighbors(cell[:-1], generalStruct)}
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
    elif 0 in cell[:-1] or 4 in cell[:-1]:  # ok this one is one the outside, level goes -1
        if cell[0] == 0:  # all separate to account for corners
            neighbors.update({(1, 2, cell[-1] - 1)})
        if cell[0] == 4:
            neighbors.update({(3, 2, cell[-1] - 1)})w
            neighbors.update({(2, 1, cell[-1] - 1)})
        if cell[1] == 4:
            neighbors.update({(2, 3, cell[-1] - 1)})
    return neighbors


for i in range(200):
    expandGrid = {}
    for coo in totalCoo:
        expandGrid.update({p: False for p in erisNeighbors(coo)})
    for p in expandGrid:
        if p not in totalCoo:
            totalCoo[p] = False

    newGrid = {}
    for coo in totalCoo:
        neighborBugCount = 0
        for pt in erisNeighbors(coo):
            if pt not in totalCoo:
                newGrid[pt] = False
                continue
            if totalCoo[pt]:
                neighborBugCount += 1
        if totalCoo[coo]:  # tests if the bug has died or not
            if not neighborBugCount == 1:
                newGrid[coo] = False
        else:  # calculates if the space should be infected or not
            if neighborBugCount in [1, 2]:
                newGrid[coo] = True
    totalCoo.update(newGrid)

bugCount = 0
for coo in totalCoo:
    if totalCoo[coo]:
        bugCount += 1
print("this shouldn't even work in actual science: %i" % bugCount)
