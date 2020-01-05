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
allKeys = set()

inFan = open(
    "C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/test.txt"
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
                    allKeys.add(c)
                    openPts.append((xVal, yVal))
                    ptsWithDoors.append((xVal, yVal))
            xVal += 1
        yVal += 1

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
    keyDistances[tuple(sorted(pair))] = iHateMazes.justDistance(keyLoc[pair[0]], ptsWithDoors, keyLoc[pair[1]])

for k in available:
    keyDistances[tuple(sorted(("start", k[-1])))] = iHateMazes.justDistance(currPos, ptsWithDoors, keyLoc[k[-1]])

print("distance from each key (including the start): %s" % keyDistances)
print("these are the keys you need for each other key: %s" % neededKeys)
statusCosts = {((), 'start'): 0}


def shortestPath(current: 'at which key', alreadyHave: set, cost: int) -> int:
    global statusCosts
    alreadyHave.add(current)
    alreadyHave = set(sorted(list(alreadyHave)))
    if allKeys.issubset(alreadyHave):
        return cost

    goodKeys = iHateMazes.findKeys(alreadyHave, neededKeys)
    shortest = float('inf')
    for canSee in goodKeys:
        savedIndex = (tuple(sorted(list(alreadyHave) + [canSee])), canSee)
        thisCost = keyDistances[tuple(sorted([current, canSee]))]
        # print('calculating we go to the key %s and we already have this list of keys: %s' % (canSee, alreadyHave))
        if savedIndex in statusCosts:
            # print('in already so yea')
            currentCost = statusCosts[(savedIndex)]
        else:
            print(statusCosts)
            currentCost = shortestPath(canSee, alreadyHave.copy(), cost + thisCost)
            statusCosts[savedIndex] = currentCost

        shortest = min(shortest, currentCost)

    return shortest

print('SEND YOUR ELVES TO BLOW UP THE MAZE AND YOUR DONE BOIII BUT PAOSIJDF: %i' % shortestPath('start', set(), 0))
print(statusCosts)

# IF YOU DONT WANT TO WAIT FOR IT TO CALC THE DISTANCES, USE THIS:
keyDistances = {('y', 'n'): 368, ('y', 'x'): 36, ('y', 'd'): 386, ('y', 'u'): 118, ('y', 'a'): 48, ('y', 'o'): 184,
                ('y', 'q'): 308, ('y', 'm'): 328, ('y', 'f'): 664, ('y', 'z'): 722, ('y', 'k'): 648, ('y', 'h'): 288,
                ('y', 'e'): 310, ('y', 't'): 682, ('y', 'w'): 630, ('y', 'l'): 700, ('y', 'p'): 736, ('y', 'i'): 614,
                ('y', 'g'): 594, ('y', 'c'): 576, ('y', 's'): 546, ('y', 'r'): 438, ('y', 'v'): 420, ('y', 'j'): 490,
                ('y', 'b'): 402, ('n', 'x'): 332, ('n', 'd'): 22, ('n', 'u'): 258, ('n', 'a'): 320, ('n', 'o'): 284,
                ('n', 'q'): 152, ('n', 'm'): 100, ('n', 'f'): 470, ('n', 'z'): 528, ('n', 'k'): 454, ('n', 'h'): 98,
                ('n', 'e'): 120, ('n', 't'): 488, ('n', 'w'): 436, ('n', 'l'): 506, ('n', 'p'): 542, ('n', 'i'): 420,
                ('n', 'g'): 400, ('n', 'c'): 382, ('n', 's'): 352, ('n', 'r'): 248, ('n', 'v'): 230, ('n', 'j'): 300,
                ('n', 'b'): 212, ('x', 'd'): 350, ('x', 'u'): 82, ('x', 'a'): 12, ('x', 'o'): 148, ('x', 'q'): 272,
                ('x', 'm'): 292, ('x', 'f'): 628, ('x', 'z'): 686, ('x', 'k'): 612, ('x', 'h'): 252, ('x', 'e'): 274,
                ('x', 't'): 646, ('x', 'w'): 594, ('x', 'l'): 664, ('x', 'p'): 700, ('x', 'i'): 578, ('x', 'g'): 558,
                ('x', 'c'): 540, ('x', 's'): 510, ('x', 'r'): 402, ('x', 'v'): 384, ('x', 'j'): 454, ('x', 'b'): 366,
                ('d', 'u'): 276, ('d', 'a'): 338, ('d', 'o'): 302, ('d', 'q'): 170, ('d', 'm'): 118, ('d', 'f'): 488,
                ('d', 'z'): 546, ('d', 'k'): 472, ('d', 'h'): 116, ('d', 'e'): 138, ('d', 't'): 506, ('d', 'w'): 454,
                ('d', 'l'): 524, ('d', 'p'): 560, ('d', 'i'): 438, ('d', 'g'): 418, ('d', 'c'): 400, ('d', 's'): 370,
                ('d', 'r'): 266, ('d', 'v'): 248, ('d', 'j'): 318, ('d', 'b'): 230, ('u', 'a'): 70, ('u', 'o'): 74,
                ('u', 'q'): 198, ('u', 'm'): 218, ('u', 'f'): 554, ('u', 'z'): 612, ('u', 'k'): 538, ('u', 'h'): 178,
                ('u', 'e'): 200, ('u', 't'): 572, ('u', 'w'): 520, ('u', 'l'): 590, ('u', 'p'): 626, ('u', 'i'): 504,
                ('u', 'g'): 484, ('u', 'c'): 466, ('u', 's'): 436, ('u', 'r'): 328, ('u', 'v'): 310, ('u', 'j'): 380,
                ('u', 'b'): 292, ('a', 'o'): 136, ('a', 'q'): 260, ('a', 'm'): 280, ('a', 'f'): 616, ('a', 'z'): 674,
                ('a', 'k'): 600, ('a', 'h'): 240, ('a', 'e'): 262, ('a', 't'): 634, ('a', 'w'): 582, ('a', 'l'): 652,
                ('a', 'p'): 688, ('a', 'i'): 566, ('a', 'g'): 546, ('a', 'c'): 528, ('a', 's'): 498, ('a', 'r'): 390,
                ('a', 'v'): 372, ('a', 'j'): 442, ('a', 'b'): 354, ('o', 'q'): 224, ('o', 'm'): 244, ('o', 'f'): 580,
                ('o', 'z'): 638, ('o', 'k'): 564, ('o', 'h'): 204, ('o', 'e'): 226, ('o', 't'): 598, ('o', 'w'): 546,
                ('o', 'l'): 616, ('o', 'p'): 652, ('o', 'i'): 530, ('o', 'g'): 510, ('o', 'c'): 492, ('o', 's'): 462,
                ('o', 'r'): 354, ('o', 'v'): 336, ('o', 'j'): 406, ('o', 'b'): 318, ('q', 'm'): 112, ('q', 'f'): 448,
                ('q', 'z'): 506, ('q', 'k'): 432, ('q', 'h'): 72, ('q', 'e'): 94, ('q', 't'): 466, ('q', 'w'): 414,
                ('q', 'l'): 484, ('q', 'p'): 520, ('q', 'i'): 398, ('q', 'g'): 378, ('q', 'c'): 360, ('q', 's'): 330,
                ('q', 'r'): 222, ('q', 'v'): 204, ('q', 'j'): 274, ('q', 'b'): 186, ('m', 'f'): 430, ('m', 'z'): 488,
                ('m', 'k'): 414, ('m', 'h'): 58, ('m', 'e'): 80, ('m', 't'): 448, ('m', 'w'): 396, ('m', 'l'): 466,
                ('m', 'p'): 502, ('m', 'i'): 380, ('m', 'g'): 360, ('m', 'c'): 342, ('m', 's'): 312, ('m', 'r'): 208,
                ('m', 'v'): 190, ('m', 'j'): 260, ('m', 'b'): 172, ('f', 'z'): 58, ('f', 'k'): 16, ('f', 'h'): 394,
                ('f', 'e'): 416, ('f', 't'): 18, ('f', 'w'): 34, ('f', 'l'): 36, ('f', 'p'): 72, ('f', 'i'): 50,
                ('f', 'g'): 70, ('f', 'c'): 88, ('f', 's'): 118, ('f', 'r'): 544, ('f', 'v'): 526, ('f', 'j'): 596,
                ('f', 'b'): 508, ('z', 'k'): 74, ('z', 'h'): 452, ('z', 'e'): 474, ('z', 't'): 40, ('z', 'w'): 92,
                ('z', 'l'): 22, ('z', 'p'): 14, ('z', 'i'): 108, ('z', 'g'): 128, ('z', 'c'): 146, ('z', 's'): 176,
                ('z', 'r'): 602, ('z', 'v'): 584, ('z', 'j'): 654, ('z', 'b'): 566, ('k', 'h'): 378, ('k', 'e'): 400,
                ('k', 't'): 34, ('k', 'w'): 18, ('k', 'l'): 52, ('k', 'p'): 88, ('k', 'i'): 34, ('k', 'g'): 54,
                ('k', 'c'): 72, ('k', 's'): 102, ('k', 'r'): 528, ('k', 'v'): 510, ('k', 'j'): 580, ('k', 'b'): 492,
                ('h', 'e'): 34, ('h', 't'): 412, ('h', 'w'): 360, ('h', 'l'): 430, ('h', 'p'): 466, ('h', 'i'): 344,
                ('h', 'g'): 324, ('h', 'c'): 306, ('h', 's'): 276, ('h', 'r'): 162, ('h', 'v'): 144, ('h', 'j'): 214,
                ('h', 'b'): 126, ('e', 't'): 434, ('e', 'w'): 382, ('e', 'l'): 452, ('e', 'p'): 488, ('e', 'i'): 366,
                ('e', 'g'): 346, ('e', 'c'): 328, ('e', 's'): 298, ('e', 'r'): 152, ('e', 'v'): 134, ('e', 'j'): 204,
                ('e', 'b'): 92, ('t', 'w'): 52, ('t', 'l'): 18, ('t', 'p'): 54, ('t', 'i'): 68, ('t', 'g'): 88,
                ('t', 'c'): 106, ('t', 's'): 136, ('t', 'r'): 562, ('t', 'v'): 544, ('t', 'j'): 614, ('t', 'b'): 526,
                ('w', 'l'): 70, ('w', 'p'): 106, ('w', 'i'): 16, ('w', 'g'): 36, ('w', 'c'): 54, ('w', 's'): 84,
                ('w', 'r'): 510, ('w', 'v'): 492, ('w', 'j'): 562, ('w', 'b'): 474, ('l', 'p'): 36, ('l', 'i'): 86,
                ('l', 'g'): 106, ('l', 'c'): 124, ('l', 's'): 154, ('l', 'r'): 580, ('l', 'v'): 562, ('l', 'j'): 632,
                ('l', 'b'): 544, ('p', 'i'): 122, ('p', 'g'): 142, ('p', 'c'): 160, ('p', 's'): 190, ('p', 'r'): 616,
                ('p', 'v'): 598, ('p', 'j'): 668, ('p', 'b'): 580, ('i', 'g'): 20, ('i', 'c'): 38, ('i', 's'): 68,
                ('i', 'r'): 494, ('i', 'v'): 476, ('i', 'j'): 546, ('i', 'b'): 458, ('g', 'c'): 18, ('g', 's'): 48,
                ('g', 'r'): 474, ('g', 'v'): 456, ('g', 'j'): 526, ('g', 'b'): 438, ('c', 's'): 30, ('c', 'r'): 456,
                ('c', 'v'): 438, ('c', 'j'): 508, ('c', 'b'): 420, ('s', 'r'): 426, ('s', 'v'): 408, ('s', 'j'): 478,
                ('s', 'b'): 390, ('r', 'v'): 22, ('r', 'j'): 56, ('r', 'b'): 244, ('v', 'j'): 74, ('v', 'b'): 226,
                ('j', 'b'): 296, ('start', 'h'): 10, ('start', 'e'): 32, ('start', 'q'): 64,
                ('start', 'u'): 170, ('start', 'o'): 196, ('start', 'a'): 232, ('start', 'x'): 244}
