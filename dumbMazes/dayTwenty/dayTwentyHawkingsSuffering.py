"""ok so im going to assume that
there are no two consecutive wormholes"""
from iHateMazes import *

validPlaces = []  # list of tuples, and empty places are in the coordinate system
ptsAndWormholes = {}  # each point is which wormhole? (ill make another good one later)

# WHAT IS THIS FILE PROCESSING
with open('data stuff/plutoIsntAPlanet') as data:
    yVal = 0
    mazeList = []
    for line in data:
        mazeList.append(list(line.rstrip()))
        xVal = 0
        wormHoleCount = 0
        nextPtIsWormhole = False
        for v, c in enumerate(line):
            if c == '.':
                if nextPtIsWormhole:
                    if wormholeId not in ptsAndWormholes:
                        ptsAndWormholes[wormholeId] = [(xVal, yVal)]
                    else:
                        ptsAndWormholes[wormholeId].append((xVal, yVal))
                    nextPtIsWormhole = False
                elif line[v + 1].isalpha():  # if the wormholeid was declared after the point
                    if line[v + 1: v + 3] not in ptsAndWormholes:
                        ptsAndWormholes[line[v + 1: v + 3]] = [(xVal, yVal)]
                    else:
                        ptsAndWormholes[line[v + 1: v + 3]].append((xVal, yVal))
                validPlaces.append((xVal, yVal))
            elif c.isalpha():  # this will get all the horizontal wormholes
                wormHoleCount += 1
                if wormHoleCount == 1:
                    wormholeId = c
                    fromThisXVal = xVal  # only add if the two are consecutive
                elif wormHoleCount == 2:
                    if xVal == fromThisXVal + 1:
                        wormholeId += c
                        nextPtIsWormhole = True
                    wormHoleCount = 0  # reset is no matter what
            else:
                nextPtIsWormhole = False  # its done. no more wormholes
            xVal += 1
        yVal += 1

    conformLen = max([len(l) for l in mazeList])
    for line in mazeList:
        if len(line) < conformLen:
            line.extend([' ' for i in range(conformLen - len(line))])

    print(mazeList)
    xVal = 0  # now we gon check for vertical wormholes
    wormHoleCount = 0
    for column in zip(*mazeList):
        yVal = 0
        for v, c in enumerate(column):
            if c == '.':
                if nextPtIsWormhole:
                    if wormholeId not in ptsAndWormholes:
                        ptsAndWormholes[wormholeId] = [(xVal, yVal)]
                    else:
                        ptsAndWormholes[wormholeId].append((xVal, yVal))
                    nextPtIsWormhole = False
                elif column[v + 1].isalpha():
                    if ''.join(column[v + 1: v + 3]) not in ptsAndWormholes:
                        ptsAndWormholes[''.join(column[v + 1: v + 3])] = [(xVal, yVal)]
                    else:
                        ptsAndWormholes[''.join(column[v + 1: v + 3])].append((xVal, yVal))
                validPlaces.append((xVal, yVal))
            elif c.isalpha():
                wormHoleCount += 1
                if wormHoleCount == 1:
                    wormholeId = c
                    fromThisYVal = yVal
                elif wormHoleCount == 2:
                    if yVal == fromThisYVal + 1:
                        wormholeId += c
                        nextPtIsWormhole = True
                    wormHoleCount = 0
            else:
                nextPtIsWormhole = False
            yVal += 1
        xVal += 1

print(ptsAndWormholes)
start, end = ptsAndWormholes['AA'][0], ptsAndWormholes['ZZ'][0]
del ptsAndWormholes['AA']
del ptsAndWormholes['ZZ']


def wormholeNeighbors(pt, ptList):
    possibleNeighbors = {
        (pt[0] - 1, pt[1]),
        (pt[0] + 1, pt[1]),
        (pt[0], pt[1] - 1),
        (pt[0], pt[1] + 1),
    }
    goodNeighbors = possibleNeighbors.intersection(ptList)
    for value in ptsAndWormholes.values():
        if pt in value:
            goodNeighbors.add(value[not value.index(pt)][:2])
    return goodNeighbors


def partOneWormholes(startPt, ptList, goal) -> int:
    frontier = {startPt}
    visited = {startPt}
    moveCount = 0
    while frontier:
        inLine = set()
        for pt in frontier:
            for p in wormholeNeighbors(pt, ptList):
                if p not in visited:
                    inLine.add(p)
                visited.add(p)

        moveCount += 1
        frontier = inLine
        if goal in frontier:
            return moveCount


print('why did we even land on this accursed place: %i' % partOneWormholes(start, validPlaces, end))
