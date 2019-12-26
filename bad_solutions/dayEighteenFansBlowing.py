"""neptune just reminds me of spongebob
WHO LIVES IN A PINEAPPLE UNDER THE SEA
maybe numpy would be good but heck that"""

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

def goToPos(curr: "coordinate", ptList, goal) -> "amt of movement needed":
    moveCount = 0
    frontier = [curr]  # or toBeProcessed
    visited = [curr]
    while frontier:  # while there still is space
        inLine = []
        for pt in frontier:
            goodPts = [p for p in ptList if p not in visited]
            visited.extend(findNeighbors(pt, goodPts))
            inLine.extend(findNeighbors(pt, goodPts))
        moveCount += 1
        frontier = inLine
        if goal in frontier:
            return moveCount
    return 0  # you just cant go there.

def keyEval():
    keyDistanceDic = {}  # order matters- key a and key b both unblock different paths
    for v, k in enumerate(keyLoc):
        forThisKey = {}
        goodPts = placesToGo[:]
        for d in assoDoorLoc:
            if d[-1].lower() == k[-1]:
                goodPts.append(d[:-1])

        for ke in keyLoc[:v] + keyLoc[v+1:]:
            if goToPos(k[:-1], goodPts, ke[:-1]):
                forThisKey[ke] = goToPos(k[:-1], goodPts, ke[:-1])
                continue
            else:
                forThisKey[ke] = 0 #you cant go from this key to that key
        keyDistanceDic[k[-1]] = forThisKey
    return keyDistanceDic

def findAvailable():
    available = {}
    for k in keyLoc:
        if goToPos(currPos, placesToGo, k[:-1]):
            available[k[-1]] = goToPos(currPos, placesToGo, k[:-1])

    return available

placesToGo = []  # itll be a list of tuples
keyLoc = []
assoDoorLoc = []

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
                placesToGo.append((xVal, yVal))
            elif c == "@":
                placesToGo.append((xVal, yVal))
                currPos = (xVal, yVal)
            else:
                if c.upper() == c:  # door found
                    assoDoorLoc.append(
                        (xVal, yVal, c)
                    )  # itll be added to placesToGo later
                else:  # key instead
                    keyLoc.append((xVal, yVal, c))
                    placesToGo.append((xVal, yVal))
            xVal += 1
        yVal += 1

# PART 1 OMG THIS IS WAY TOO LONG
print(keyEval())
print(findAvailable())
