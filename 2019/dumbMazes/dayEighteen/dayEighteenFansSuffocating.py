"""neptune just reminds me of spongebob
WHO LIVES IN A PINEAPPLE UNDER THE SEA
maybe numpy would be good but heck that"""
from heapq import heappush, heappop
from collections import deque
from itertools import combinations
import dumbMazes.iHateMazes as iHateMazes

# STUPID GOSH OOF PART 2 AAAAAAAA
ptsWithDoors = set()
keyLoc = {}  # it includes the start positions because technically they are a valid position to be at
doorLoc = {}
allKeys = set()
robotStartPos = []
startPosCount = 0

with open('poPoPoseidon.txt') as stuff:
    yVal = 0
    for lin in reversed(stuff.readlines()):
        xVal = 0
        lin = lin.rstrip()
        for c in list(lin):
            if c == '#':
                xVal += 1
                continue
            elif c == "@":
                robotStartPos.append((xVal, yVal))
                keyLoc['start' + str(startPosCount)] = (xVal, yVal)
                startPosCount += 1  # they go from down to up, left to right.
            elif c.isalpha():
                if c.upper() == c:  # door found
                    doorLoc[c] = (xVal, yVal)
                else:  # key instead
                    keyLoc[c] = (xVal, yVal)
                    allKeys.add(c)
            ptsWithDoors.add((xVal, yVal))
            xVal += 1
        yVal += 1

# each of these are associated by index, which probably is the wrong thing to do oof
canGetKeys = []  # the list of initially available keys
totalRoomKeys = []  # the list of total keys for each "room"
requirements = {}
for startPos in robotStartPos:  # TODO: clean this up gosh darn it
    blockedYet = False
    available = []
    roomKeys = set()
    processList = [startPos]
    usedBefore = {startPos}
    keysLeft = keyLoc.copy()  # to prevent searching the same key twice

    while processList:
        inLine = []
        for p in processList:
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
                # print(k, 'doesnt need any keys to get in')
                killList.append(k)
            elif keyLoc[k] in usedBefore:
                roomKeys.add(k)
                killList.append(k)
        for target in killList:
            del keysLeft[target]

    canGetKeys.append(available)
    totalRoomKeys.append(roomKeys)

killList = []
for req in requirements:
    if req.startswith('start'):
        killList.append(req)
for target in killList:  # all these three for loops eliminate the unnecessary stuff
    del requirements[target]

for v, s in enumerate(canGetKeys):
    for el in s:
        if el.startswith('start'):
            canGetKeys[v].remove(el)

keyDistances = {}
for v, l in enumerate(totalRoomKeys):  # calculates distances for keys (room specific)
    for pair in combinations(l, 2):
        keyDistances[tuple(sorted(pair))] = iHateMazes.justDistance(keyLoc[pair[0]], ptsWithDoors, keyLoc[pair[1]])

for key in allKeys:  # calculates requirements to get to each key
    neededKeys = []
    for setOfKeys in totalRoomKeys:
        if key in setOfKeys:
            startPos = [s for s in setOfKeys if s.startswith('start')][0]
            path = iHateMazes.goToPos(keyLoc[startPos], ptsWithDoors, keyLoc[key])[1]
            neededKeys = []
            for d in doorLoc:
                if doorLoc[d] in path:
                    neededKeys.append(d.lower())
    requirements[key] = neededKeys


# ACTUALLY MAKING THE GRAPH AND EXPLORING IT
def makeFinal(initial, keyToGet):  # just makes the format for the graph down below
    resultingKeys = initial[0] + (keyToGet,)
    for v, keyList in enumerate(totalRoomKeys):
        if keyToGet in keyList:
            resultingPos = initial[1][:v] + (keyToGet,) + initial[1][v + 1:]
    return tuple(sorted(resultingKeys)), resultingPos


def statusNeighbors(status, allStatuses):  # same as keyNeighbors for p1
    canSeeKeys = iHateMazes.findKeys(status[0], requirements)
    goodNeighbors = []
    for testKey in canSeeKeys:
        testee = makeFinal(status, testKey)
        if testee in allStatuses:
            goodNeighbors.append(testee)
    return goodNeighbors


start = ((), ('start0', 'start1', 'start2', 'start3'))  # the same thing as the first but four pos
statusGraphs = {start}
toBeProcessed = deque([start])
while toBeProcessed:
    currStatus = toBeProcessed.popleft()
    for possibleKey in iHateMazes.findKeys(currStatus[0], requirements):
        resultingStatus = makeFinal(currStatus, possibleKey)
        if resultingStatus not in statusGraphs:
            statusGraphs.add(resultingStatus)
            toBeProcessed.append(resultingStatus)

costs = {start: 0}
statusQueue = [(0, start)]
while statusQueue:
    moves, current = heappop(statusQueue)
    if len(current[0]) == len(allKeys):
        robotCost = moves
        break
    for nextStatus in statusNeighbors(current, statusGraphs):
        for v, p in enumerate(current[1]):  # detects what change in the position it was
            if nextStatus[1][v] != p:
                pair = tuple(sorted((p, nextStatus[1][v])))
                break

        newCost = costs[current] + keyDistances[pair]
        if nextStatus not in costs or newCost < costs[nextStatus]:
            costs[nextStatus] = newCost
            heappush(statusQueue, (newCost, nextStatus))

print('beepity boopity the robots will take a minimum of %i steps' % robotCost)
