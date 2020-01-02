"""this is the optimized solution
it came after a week of work, crying my eyeballs out,
hundreds of reddit comments, and begging for help on discord"""
from queue import PriorityQueue, Queue
from itertools import combinations
import iHateMazes
from sys import exit

openPts = []  # itll be a list of tuples
ptsWithDoors = []
keyLoc = {}
DoorLoc = {}
allKeys = []

inFan = open(
    "C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/poPoseidon"
)

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

available = []
for k in keyLoc:
    try:
        iHateMazes.goToPos(currPos, openPts, keyLoc[k])
        available.append(k)
    except KeyError:  # it gives me this it it cant find the key with the points
        pass

neededKeys = {}  # for each key of the dictionary, you need the values(empty if none)

for k in keyLoc:
    print("processing key %s" % k)
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

print("distance from each key (including the start): %s" % keyDistances)
print("these are the keys you need for each other key: %s" % neededKeys)