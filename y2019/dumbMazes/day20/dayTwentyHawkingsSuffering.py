"""
ok so im going to assume that
there are no two consecutive wormholes
"""
validPlaces = []  # list of tuples, and empty places are in the coordinate system
ptsAndWormholes = {}  # each point is which wormhole?

with open('plutoIsntAPlanet.txt') as maze:
    mazeList = []
    yVal = 0
    for row in maze.readlines():
        mazeList.append(list(row.rstrip()))
        xVal = 0
        wormholeDetected = False
        for v, c in enumerate(row.rstrip()):
            if c == '.':
                if row[v - 1].isalpha() or row[v + 1].isalpha():
                    if row[v - 1].isalpha():
                        wormholeId = ''.join(row[v - 2:v])
                    elif row[v + 1].isalpha():
                        wormholeId = ''.join(row[v + 1:v + 3])
                    wormholeDetected = True

                if wormholeDetected:
                    if wormholeId not in ptsAndWormholes:  # True is outside, False is inside
                        ptsAndWormholes[wormholeId] = [(xVal, yVal, xVal == 2 or xVal == len(row.rstrip()) - 1 - 2)]
                    else:
                        ptsAndWormholes[wormholeId].append((xVal, yVal, xVal == 2 or xVal == len(row.rstrip()) - 1 - 2))
                    wormholeDetected = False
                validPlaces.append((xVal, yVal))
            xVal += 1
        yVal += 1

    conformLen = max([len(x) for x in mazeList])
    for v, row in enumerate(mazeList):
        if len(row) < conformLen:
            mazeList[v].extend([' ' for i in range(conformLen - len(row))])

    xVal = 0
    for column in zip(*mazeList):
        yVal = 0
        for v, c in enumerate(column):
            if c == '.':
                if column[v - 1].isalpha() or column[v + 1].isalpha():
                    if column[v - 1].isalpha():
                        wormholeId = ''.join(column[v - 2:v])
                    elif column[v + 1].isalpha():
                        wormholeId = ''.join(column[v + 1:v + 3])
                    wormholeDetected = True

                if wormholeDetected:
                    if wormholeId not in ptsAndWormholes:
                        ptsAndWormholes[wormholeId] = [(xVal, yVal, yVal == 2 or yVal == len(column) - 1 - 2)]
                    else:
                        ptsAndWormholes[wormholeId].append((xVal, yVal, yVal == 2 or yVal == len(column) - 1 - 2))
                    wormholeDetected = False
            yVal += 1
        xVal += 1

start, end = ptsAndWormholes['AA'][0][:-1], ptsAndWormholes['ZZ'][0][:-1]
del ptsAndWormholes['AA']
del ptsAndWormholes['ZZ']
linkedPts = {}
for pair in ptsAndWormholes.values():
    linkedPts[pair[0][:-1]] = (pair[1][:-1], pair[0][-1])
    linkedPts[pair[1][:-1]] = (pair[0][:-1], pair[1][-1])

def partOneNeighbors(pt, ptList):  # this one still uses ptsAndWormholes
    possibleNeighbors = {
        (pt[0] - 1, pt[1]),
        (pt[0] + 1, pt[1]),
        (pt[0], pt[1] - 1),
        (pt[0], pt[1] + 1),
    }
    goodNeighbors = possibleNeighbors.intersection(ptList)
    for value in ptsAndWormholes.values():
        justPoints = [v[:-1] for v in value]
        if pt in justPoints:
            goodNeighbors.add(justPoints[not justPoints.index(pt)][:2])
    return goodNeighbors


# PART 1
def partOneWormholes(startPt: tuple, ptList: list, goal: tuple) -> int:  # TODO: YOUR CIVICS PROJECT
    frontier = {startPt}
    visited = {startPt}
    moveCount = 0
    while frontier:
        inLine = set()
        for pt in frontier:
            for p in partOneNeighbors(pt, ptList):
                if p not in visited:
                    inLine.add(p)
                visited.add(p)

        moveCount += 1
        frontier = inLine
        if goal in frontier:
            return moveCount


print('why did we even land on this accursed place: %i' % partOneWormholes(start, validPlaces, end))

# PART 2


def partTwoNeighbors(pt, ptList):
    possibleNeighbors = {
        (pt[0][0] - 1, pt[0][1]),
        (pt[0][0] + 1, pt[0][1]),
        (pt[0][0], pt[0][1] - 1),
        (pt[0][0], pt[0][1] + 1),
    }
    goodNeighbors = {(p, pt[-1]) for p in possibleNeighbors.intersection(ptList)}
    try:
        resultingPt = linkedPts[pt[0]]
    except KeyError:
        return goodNeighbors
    if not (resultingPt[1] and pt[1] == 0):
        goodNeighbors.add((resultingPt[0], pt[1] - 1 if resultingPt[1] else pt[1] + 1))
    return goodNeighbors


def partTwoWormholes(start: tuple, ptList: list, goal: tuple) -> int:
    frontier = {(start, 0)}
    visited = {(start, 0)}
    moveCount = 0
    while frontier:
        inLine = set()
        for pt in frontier:
            for p in partTwoNeighbors(pt, ptList):
                if p not in visited:
                    inLine.add(p)
                visited.add(p)

        moveCount += 1
        frontier = inLine
        if goal in frontier:
            return moveCount


# TODO: legit this thing isnt optimized someone help
print('actually why in blue blazes are u doing this maze: %i' % partTwoWormholes(start, validPlaces, (end, 0)))
