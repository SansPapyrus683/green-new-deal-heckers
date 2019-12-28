"""neptune just reminds me of spongebob
WHO LIVES IN A PINEAPPLE UNDER THE SEA
maybe numpy would be good but heck that"""
from queue import PriorityQueue
from itertools import combinations

openPts = []  # itll be a list of tuples
ptsWithDoors = []
keyLoc = {}
assoDoorLoc = {}

inFan = open("C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/test.txt")
# inFan = open('data stuff/poPoSeidon')
with inFan as stuff:
    yVal = 0
    for l in reversed(stuff.readlines()):
        xVal = 0
        l = l.rstrip()
        for c in list(l):
            if c == "#":
                pass
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


def manhattan(a, b):
    """shameless copied from some place other than stackoverflow
    they called me a madman"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def goToPos(start, ptList, goal):
    # path that goes to the thing along with the amt of moves needed
    frontier = PriorityQueue()
    frontier.put([0, start])
    camefrom = {}
    camefrom[start] = None
    costSoFar = {}
    costSoFar[start] = 0

    while not frontier.empty():
        current = frontier.get()[1]

        if current == goal:
            break

        for nextPt in findNeighbors(current, ptList):
            newCost = costSoFar[current] + 1
            if nextPt not in costSoFar or newCost < costSoFar[nextPt]:
                costSoFar[nextPt] = newCost
                priority = newCost + manhattan(nextPt, goal)
                frontier.put([priority, nextPt])
                camefrom[nextPt] = current

    current = goal
    path = []
    while current != start:
        path.append(current)
        current = camefrom[current]

    return len(path), path


# PART 1 OMG THIS IS WAY TOO LONG
frontier = [currPos]
visited = [currPos]
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

neededKeys = {}  # for each key of the dictionary, you need the values(empty if none)

for k in keyLoc:
    # print('processing key %s' % k)
    keyPath = goToPos(currPos, ptsWithDoors, keyLoc[k])[1]
    keyList = []
    for d in assoDoorLoc:
        if assoDoorLoc[d] in keyPath:
            keyList.append(d.lower())

    neededKeys[k] = keyList

keyDistances = {}
for pair in combinations(keyLoc, 2):
    # print(pair)
    keyDistances[pair] = goToPos(keyLoc[pair[0]], ptsWithDoors, keyLoc[pair[1]])[0]
for k in available:
    keyDistances[("start", k[-1])] = goToPos(currPos, ptsWithDoors, keyLoc[k[-1]])[0]

print(keyDistances)
print(neededKeys)
#data strucutre- [[([collected keys], key location), [all the nodes or keys or smth you can go to i think]]]
for k in neededKeys:
    if not neededKeys[k]:
