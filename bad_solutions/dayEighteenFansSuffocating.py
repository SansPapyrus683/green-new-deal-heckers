"""neptune just reminds me of spongebob
WHO LIVES IN A PINEAPPLE UNDER THE SEA
maybe numpy would be good but heck that"""
from queue import PriorityQueue
from itertools import combinations
import iHateMazes
from sys import exit

# STUPID GOSH OOF PART 2 AAAAAAAA
openPts = []  # itll be a list of tuples
ptsWithDoors = []
keyLoc = {}  # it includes the start positions because technically they are a valid position to be at
doorLoc = {}
allKeys = []
robotStartPos = []
startPosCount = 0

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
                keyLoc['start' + str(startPosCount)] = (xVal, yVal)
                startPosCount += 1  # they go from down to up, left to right.
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

# each of these are associated by index, which probably is the wrong thing to do oof
canGetKeys = []  # the list of initially available keys
totalRoomKeys = []  # the list of total keys for each "room"
requirements = {}
for startPos in robotStartPos:
    blockedYet = False
    available = []
    roomKeys = set()
    processList = [startPos]
    usedBefore = {startPos}
    keysLeft = keyLoc.copy()  # to prevent searching the same key twice

    while processList:
        for p in processList:
            inLine = []
            for n in iHateMazes.findNeighbors(p, ptsWithDoors):
                if n not in usedBefore:
                    usedBefore.add(n)
                    inLine.append(n)
            processList = inLine

        for d in doorLoc:
            if doorLoc[d] in usedBefore:
                blockedYet = True
                continue

        killList = []
        for k in keysLeft:
            if keysLeft[k] in usedBefore and not blockedYet:
                available.append(k)
                roomKeys.add(k)
                requirements[k] = []
                print(k, 'doesnt need any keys')
                killList.append(k)
            elif keyLoc[k] in usedBefore:
                neededKeys = []
                for d in doorLoc:
                    if doorLoc[d] in usedBefore:
                        neededKeys.append(d.lower())
                requirements[k] = neededKeys
                roomKeys.add(k)
                killList.append(k)
        for target in killList:
            del keysLeft[target]

    canGetKeys.append(available)
    totalRoomKeys.append(list(roomKeys))

killList = []
for req in requirements:
    if req.startswith('start'):
        killList.append(req)

for target in killList:
    del requirements[target]

keyDistances = {}
for v, l in enumerate(totalRoomKeys):
    for pair in combinations(l, 2):
        keyDistances[pair] = iHateMazes.justDistance(keyLoc[pair[0]], ptsWithDoors, keyLoc[pair[1]])

