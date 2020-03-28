"""neptune just reminds me of spongebob
WHO LIVES IN A PINEAPPLE UNDER THE SEA
maybe numpy would be good but heck that
but anyways this isn't a really 'good' solution"""
from heapq import heappush, heappop
from collections import deque
from itertools import combinations
import sys
sys.path.insert(1, 'C:\\Users\\kevin\\OneDrive\\Documents\\GitHub\\green-new-deal-heckers\\2019\\dumbMazes')
import iHateMazes

openPts = set()  # it'll be a set of tuples
ptsWithDoors = set()
keyLoc = {}
DoorLoc = {}
allKeys = []

with open('poPoSeidon.txt') as stuff:
    yVal = 0
    for l in reversed(stuff.readlines()):
        xVal = 0
        l = l.rstrip()
        for c in list(l):
            if c == "#":
                pass
            elif c == ".":
                ptsWithDoors.add((xVal, yVal))
                openPts.add((xVal, yVal))
            elif c == "@":
                openPts.add((xVal, yVal))
                ptsWithDoors.add((xVal, yVal))
                currPos = (xVal, yVal)
            else:
                if c.upper() == c:  # door found
                    DoorLoc[c] = (xVal, yVal)
                    ptsWithDoors.add((xVal, yVal))
                else:  # key instead
                    keyLoc[c] = (xVal, yVal)
                    allKeys.append(c)
                    openPts.add((xVal, yVal))
                    ptsWithDoors.add((xVal, yVal))
            xVal += 1
        yVal += 1
    allKeys = tuple(allKeys)

available = []
for k in keyLoc:
    try:
        iHateMazes.goToPos(currPos, openPts, keyLoc[k])
        available.append(k)
    except KeyError:  # it gives me this it it cant find the key with the lightStates
        pass

neededKeys = {}  # for each key of the dictionary, you need the values(empty if none)

for k in keyLoc:
    # print("processing key %s" % k)
    keyPath = iHateMazes.goToPos(currPos, ptsWithDoors, keyLoc[k])[1]
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
    keyDistances[pair] = iHateMazes.justDistance(keyLoc[pair[0]], ptsWithDoors, keyLoc[pair[1]])

for k in available:
    keyDistances[("start", k[-1])] = iHateMazes.justDistance(currPos, ptsWithDoors, keyLoc[k[-1]])


# PART 1 OMG THIS IS WAY TOO LONG
def keyNeighbors(status, allPossibles):
    possibleKeys = iHateMazes.findKeys(status[0], neededKeys)
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


statusGraphs = {
    ((), "start")
}  # each will be ((already haved keys), current position (at which key?))

toBeProcessed = deque([()])
while toBeProcessed:
    current = toBeProcessed.popleft()
    for ke in iHateMazes.findKeys(current, neededKeys):
        gotKeys = [ke]
        gotKeys.extend(current)
        gotKeys.sort()
        gotKeys = tuple(gotKeys)
        if (gotKeys, ke) not in statusGraphs:
            statusGraphs.add((gotKeys, ke))
            toBeProcessed.append(gotKeys)

toBeProcessedKeys = [(0, ((), "start"))]
costs = {((), "start"): 0}
while toBeProcessedKeys:  # this explores the graph dijkstra-style
    moves, current = heappop(toBeProcessedKeys)
    if len(current[0]) == len(allKeys):
        lowestMovement = moves
        break
    for curProcess in keyNeighbors(current, statusGraphs):
        a, b = current[1], curProcess[1]
        if (a, b) in keyDistances:
            thisCost = keyDistances[a, b]
        else:
            thisCost = keyDistances[b, a]
        newCost = costs[current] + thisCost
        if curProcess not in costs or newCost < costs[curProcess]:
            costs[curProcess] = newCost
            priority = newCost
            heappush(toBeProcessedKeys, (priority, curProcess))

print("JUST WANDER THE MAZE HECK IT: %i" % lowestMovement)
