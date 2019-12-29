"""neptune just reminds me of spongebob
WHO LIVES IN A PINEAPPLE UNDER THE SEA
maybe numpy would be good but heck that"""
from queue import PriorityQueue, Queue
from itertools import combinations
from sys import exit

openPts = []  # itll be a list of tuples
ptsWithDoors = []
keyLoc = {}
DoorLoc = {}
allKeys = []

inFan = open("C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/test.txt")
# inFan = open('C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/poPoSeidon')
with inFan as stuff:
    yVal = 0
    for l in reversed(stuff.readlines()):
        xVal = 0
        l = l.rstrip()
        for c in list(l):
            if c == "#":
                pass
            elif c == ".":
                ptsWithDoors.append((xVal, yVal))
                openPts.append((xVal, yVal))
            elif c == "@":
                openPts.append((xVal, yVal))
                ptsWithDoors.append((xVal, yVal))
                currPos = (xVal, yVal)
            else:
                if c.upper() == c:  # door found
                    DoorLoc[c] = (xVal, yVal)
                    ptsWithDoors.append((xVal, yVal))
                else:  # key instead
                    keyLoc[c] = (xVal, yVal)
                    allKeys.append(c)
                    openPts.append((xVal, yVal))
                    ptsWithDoors.append((xVal, yVal))
            xVal += 1
        yVal += 1
    allKeys = tuple(allKeys)


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
    tempFrontier = PriorityQueue()
    tempFrontier.put([0, start])
    camefrom = {start: None}  # pycharm told me to do this
    costSoFar = {start: 0}

    while not tempFrontier.empty():
        processed = tempFrontier.get()[1]

        if processed == goal:
            break

        for nextPt in findNeighbors(processed, ptList):
            newCost = costSoFar[processed] + 1
            if nextPt not in costSoFar or newCost < costSoFar[nextPt]:
                costSoFar[nextPt] = newCost
                priority = newCost + manhattan(nextPt, goal)
                tempFrontier.put([priority, nextPt])
                camefrom[nextPt] = processed

    processed = goal
    path = []
    while processed != start:
        path.append(processed)
        processed = camefrom[processed]

    return len(path), path


def justDistance(start, ptList, goal):
    frontier = [start]
    visited = [start]
    moveCount = 0
    while frontier:
        inLine = []
        for pt in frontier:
            for p in findNeighbors(pt, ptList):
                if p not in visited:
                    inLine.append(p)
                    visited.append(p)
        moveCount += 1
        frontier = inLine
        if goal in frontier:
            return moveCount


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
    print('processing key %s' % k)
    keyPath = goToPos(currPos, ptsWithDoors, keyLoc[k])[1]
    keyList = []
    for d in DoorLoc:
        if DoorLoc[d] in keyPath:
            keyList.append(d.lower())

    neededKeys[k] = keyList
for k in neededKeys:
    if k in available and neededKeys[k]:
        neededKeys[k] = []

keyDistances = {}
for pair in combinations(keyLoc, 2):
    keyDistances[pair] = justDistance(keyLoc[pair[0]], ptsWithDoors, keyLoc[pair[1]])

for k in available:
    keyDistances[("start", k[-1])] = justDistance(currPos, ptsWithDoors, keyLoc[k[-1]])

print("distance from each key (including the start): %s" % keyDistances)
print("these are the keys you need for each other key: %s" % neededKeys)

exit()

# PART 1 OMG THIS IS WAY TOO LONG
def findKeys(alreadyHave, keyRequirement=neededKeys):
    """takes a buncha keys and returns the keys you can get"""
    canGet = []
    for k in keyRequirement:
        if set(keyRequirement[k]).issubset(set(alreadyHave)) and k not in alreadyHave:
            canGet.append(k)
    return canGet


def keyNeighbors(status, allPossibles):
    possibleKeys = findKeys(status[0])
    possibleKeys.sort()
    neighbors = []
    for key in possibleKeys:
        test = [list(status[0][:]), key]
        test[0].append(key)
        test[0].sort()
        test[0] = tuple(test[0])
        test = tuple(test)
        if test in allPossibles:
            neighbors.append(test)
    return neighbors


horribleKeyGraph = [[[], "start"]]
toBeProcessed = Queue()
toBeProcessed.put(horribleKeyGraph[0])

while not toBeProcessed.empty():
    current = toBeProcessed.get()
    for ke in findKeys((current[0])):
        gotKeys = [ke]
        gotKeys.extend(current[0])
        gotKeys.sort()
        horribleKeyGraph.append([gotKeys, ke])
        toBeProcessed.put([gotKeys, ke])

for v, t in enumerate(horribleKeyGraph):
    horribleKeyGraph[v][0] = tuple(horribleKeyGraph[v][0])
horribleKeyGraph = [tuple(l) for l in horribleKeyGraph]

toBeProcessedKeys = PriorityQueue()
toBeProcessedKeys.put([0, horribleKeyGraph[0]])
costs = {horribleKeyGraph[0][:]: 0}
print(horribleKeyGraph)

while not toBeProcessedKeys.empty():
    current = toBeProcessedKeys.get()
    for next in keyNeighbors(current[1], horribleKeyGraph):
        for k in keyDistances:
            if current[1][1] in k and next[1] in k:
                thisCost = keyDistances[k]
        newCost = costs[current[1]] + thisCost
        if next not in costs or newCost < costs[next]:
            costs[next] = newCost
            priority = newCost
            toBeProcessedKeys.put([priority, next])

lowestMovement = float('inf')
for k in costs:
    if set(allKeys).issubset(set(k[0])) and costs[k] < lowestMovement:
        lowestMovement = costs[k]

print('OMG YOU COULDVE JUST WANDERED THE MAZE BUT NO YOU HAD TO DO IT A NERDY-BUTT WAY BUT HERE: %i' % lowestMovement)
