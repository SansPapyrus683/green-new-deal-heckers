"""neptune just reminds me of spongebob
WHO LIVES IN A PINEAPPLE UNDER THE SEA
maybe numpy would be good but heck that"""
from queue import Queue

openPts = []  # itll be a list of tuples
ptsWithDoors = []
keyLoc = {}
assoDoorLoc = {}

inFan = open("data stuff/test.txt")
with inFan as stuff:
    yVal = 0
    for l in reversed(stuff.readlines()):
        xVal = 0
        l = l.rstrip()
        for c in list(l):
            if c == "#":
                xVal += 1
            elif c == ".":
                openPts.append((xVal, yVal))
                ptsWithDoors.append((xVal, yVal))
            elif c == "@":
                openPts.append((xVal, yVal))
                ptsWithDoors.append((xVal, yVal))
                currPos = (xVal, yVal)
            else:
                if c.upper() == c:  # door found
                    assoDoorLoc[c] = (xVal, yVal)
                    ptsWithDoors.append((xVal, yVal))
                else:  # key instead
                    keyLoc[c] = (xVal, yVal)
                    openPts.append((xVal, yVal))
                    ptsWithDoors.append((xVal, yVal))
            xVal += 1
        yVal += 1


def findNeighbors(pt: "point", ptList: "list of good points") -> "list of neighbors":
    possibleNeighbors = [
        (pt[0] - 1, pt[1]),
        (pt[0] + 1, pt[1]),
        (pt[0], pt[1] - 1),
        (pt[0], pt[1] + 1),
    ]
    goodNeighbors = []
    for p in possibleNeighbors:
        if p in ptList:
            goodNeighbors.append(p)
    return goodNeighbors


def goToPos(start, ptList, goal):
    #path that goes to the thing along with the amt of moves needed
    frontier = Queue()
    frontier.put(start)
    camefrom = {}
    camefrom[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in findNeighbors(current, ptList):
            if next not in camefrom:
                frontier.put(next)
                camefrom[next] = current

    current = goal
    path = []
    while current != start:
        path.append(current)
        current = camefrom[current]

    return len(path), path


def findAvailable(fromPos=currPos):
    frontier = [fromPos]
    visited = [fromPos]
    available = []
    while frontier:
        inLine = []
        for pt in frontier:
            for pt in [p for p in findNeighbors(pt, openPts) if p not in visited]:
                visited.append(pt)
                inLine.append(pt)
        frontier = inLine
        for key in keyLoc:
            if keyLoc[key] in frontier:
                available.append(key)

    return available


# PART 1 OMG THIS IS WAY TOO LONG
available = findAvailable()
neededKeys = {} #for each key of the dictionary, you need the values(empty if none)

for k in keyLoc:
    #print(goToPos(keyLoc[k], ptsWithDoors, currPos))
    keyPath = goToPos(keyLoc[k], ptsWithDoors, currPos)[1]
    keyList = []
    for d in assoDoorLoc:
        if assoDoorLoc[d] in keyPath:
            keyList.append(d.lower())

    neededKeys[k] = keyList

print(neededKeys)