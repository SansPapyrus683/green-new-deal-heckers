"""neptune just reminds me of spongebob
WHO LIVES IN A PINEAPPLE UNDER THE SEA
maybe numpy would be good but heck that"""
from queue import PriorityQueue, Queue
from itertools import combinations
from sys import exit

# STUPID GOSH OOF PART 2 AAAAAAAA
openPts = []  # itll be a list of tuples
ptsWithDoors = []
keyLoc = {}
doorLoc = {}
allKeys = []
robotStartPos = []

inFan = open(
    "C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/test.txt"
)

with inFan as stuff:
    yVal = 0
    for lin in reversed(stuff.readlines()):
        xVal = 0
        lin = lin.rstrip()
        for c in list(lin):
            if c == '#':
                xVal += 1
                continue
            elif c == ".":
                openPts.append((xVal, yVal))
            elif c == "@":
                openPts.append((xVal, yVal))
                robotStartPos.append((xVal, yVal))
            else:
                if c.upper() == c:  # door found
                    doorLoc[c] = (xVal, yVal)
                else:  # key instead
                    keyLoc[c] = (xVal, yVal)
                    allKeys.append(c)
                    openPts.append((xVal, yVal))
            ptsWithDoors.append((xVal, yVal))
            xVal += 1
        yVal += 1
    allKeys = tuple(allKeys)


def findNeighbors(pt: "the point to find neighbors for", ptList: "list of good points"):
    possibleNeighbors = {
        (pt[0] - 1, pt[1]),
        (pt[0] + 1, pt[1]),
        (pt[0], pt[1] - 1),
        (pt[0], pt[1] + 1),
    }
    goodNeighbors = set()
    for pt in possibleNeighbors:
        if pt in ptList:
            goodNeighbors.add(pt)
    return goodNeighbors


def manhattan(a, b):
    """shameless copied from some place other than stackoverflow
    they called me a madman"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def goToPos(start, ptList, goal):
    # path that goes to the thing along with the amt of moves needed
    tempFrontier = PriorityQueue()
    tempFrontier.put([0, start])
    cameFromPos = {start: None}  # pycharm told me to do this
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
                cameFromPos[nextPt] = processed

    processed = goal
    path = set()
    while processed != start:
        path.add(processed)
        processed = cameFromPos[processed]

    return len(path), path


def justDistance(start, ptList, goal):
    frontier = {start}
    visited = {start}
    moveCount = 0
    while frontier:
        inLine = set()
        for pt in frontier:
            for p in findNeighbors(pt, ptList):
                if p not in visited:
                    inLine.add(p)
                visited.add(p)

        moveCount += 1
        frontier = inLine
        if goal in frontier:
            return moveCount


# each of these are associated by index, which probably is the wrong thing to do oof
assoAvailable = []  # the list of initially available keys
assoTotal = []  # the list of total keys for each "room"
for startPos in robotStartPos:
    blockedYet = False
    available = []
    roomKeys = []
    processList = [startPos]
    usedBefore = [startPos]
    while processList:
        for p in processList:
            inLine = []
            for n in findNeighbors(p, ptsWithDoors):
                if n not in usedBefore:
                    usedBefore.append(n)
                    inLine.append(n)
            processList = inLine

    for d in doorLoc:
        if doorLoc[d] in usedBefore:
            blockedYet = True
            continue

    for k in keyLoc:
        if keyLoc[k] in usedBefore and not blockedYet:
            available.append(k)
            roomKeys.append(k)
        elif keyLoc[k] in usedBefore:
            roomKeys.append(k)

    assoAvailable.append(available)
    assoTotal.append(roomKeys)

print(assoAvailable)
print(assoTotal)