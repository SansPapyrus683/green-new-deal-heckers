"""
Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.
^ without this, i'd probably die lol
"""
import re
from typing import List
from math import sqrt
import numpy as np


# returns 0 if they don't line up at any place, 
# 1 if they match like for the first edge pair and 2 for the second
def lineUp(edge1: List[List[str]], edge2: List[List[str]]) -> int:
    """
    returns 0 if they can't line up at all
    returns 1 if the first edge pair of edge1 is valid
    and 2 if the second edge pair is valid
    """
    otherEdges = edge2[0] + edge2[1]
    for e in edge1[0]:
        for otherE in otherEdges:
            if e == otherE or e == otherE[::-1]:
                return 1
    for e in edge1[1]:
        for otherE in otherEdges:
            if e == otherE or e == otherE[::-1]:
                return 2
    return 0


def verticalNeighbors(side: int, r: int, c: int) -> List[List[int]]:
    return [p for p in [[r + 1, c], [r - 1, c]] if 0 <= p[0] < side]


def horizontalNeighbors(side: int, r: int, c: int) -> List[List[int]]:
    return [p for p in [[r, c + 1], [r, c - 1]] if 0 <= p[1] < side]


def neighbors(side: int, r: int, c: int) -> List[List[int]]:
    return verticalNeighbors(side, r, c) + horizontalNeighbors(side, r, c)


def orientations(tile: List[str]) -> List[List[str]]:
    """
    gives all possible ways a tile can be in
    copied from https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    """
    possible = []
    rotated = tile.copy()
    for _ in range(4):
        possible.append(rotated)
        rotated = list(''.join(r) for r in zip(*rotated[::-1]))

    rotated = [r for r in reversed(tile)]
    for _ in range(4):
        possible.append(rotated)
        rotated = list(''.join(r) for r in zip(*rotated[::-1]))

    rotated = [r[::-1] for r in tile]
    for _ in range(4):
        possible.append(rotated)
        rotated = list(''.join(r) for r in zip(*rotated[::-1]))
    return possible


tiles = {}
with open('gonnaStayUp.txt') as read:
    for rawTile in read.read().split('\n\n'):
        rawTile = rawTile.strip().split('\n')
        tile = []
        tiles[int(''.join(c for c in rawTile[0] if c.isdigit()))] = rawTile[1:]
    sideLen = int(sqrt(len(tiles)))
    assert sideLen == sqrt(len(tiles)), 'just please give me a square'

edges = {}
for tileID, tile in tiles.items():
    edges[tileID] = [[tile[0], tile[-1]], [''.join(r[0] for r in tile), ''.join(r[-1] for r in tile)]]

adjacentIDs = {}
prod = 1
start = -1
for id1, tile1 in edges.items():
    adjacentIDs[id1] = [[], []]
    matches = []
    for id2, tile2 in edges.items():
        if id1 == id2:
            continue
        result = lineUp(tile1, tile2)
        if result != 0:
            matches.append(result)
            adjacentIDs[id1][result - 1].append(id2)
    # only matches 2, so it must be a corner piece
    if sorted(matches) == [1, 2]:
        start = id1  # idk, just assign a random corner for our start
        prod *= id1
assert start != -1, "there's gotta be a corner bro"
print("this is the worst camera design ever made in the history of mankind: %i" % prod)

picIDs = np.full((sideLen, sideLen), -1)
picIDs[0][0] = start
frontier = [[[0, 0], start]]
while frontier:  # first build the picture out of pure IDs
    curr = frontier.pop(0)
    upDown, leftRight = [set(i) for i in adjacentIDs[curr[-1]]]
    row, col = curr[0]
    firstMatch = len(upDown)
    secondMatch = len(leftRight)
    vNeighbors = verticalNeighbors(sideLen, row, col)
    hNeighbors = horizontalNeighbors(sideLen, row, col)
    for vn in vNeighbors:
        val = picIDs[vn[0]][vn[1]]
        if val != -1 and val not in upDown:
            upDown, leftRight = leftRight, upDown
            break

    # clear out the ones that've alr been processed, then fill in the undone ones
    for vr, vc in vNeighbors:
        if picIDs[vr, vc] != -1:
            upDown.remove(picIDs[vr, vc])
    for vr, vc in vNeighbors:
        if picIDs[vr, vc] == -1:
            picIDs[vr, vc] = upDown.pop()
            frontier.append([[vr, vc], picIDs[vr, vc]])

    for hr, hc in hNeighbors:
        if picIDs[hr, hc] != -1:
            leftRight.remove(picIDs[hr, hc])
    for hr, hc in hNeighbors:
        if picIDs[hr, hc] == -1:
            picIDs[hr, hc] = leftRight.pop()
            frontier.append([[hr, hc], picIDs[hr, hc]])

# try all the starting orientations because we don't really know which one it is
for startingO in orientations(tiles[picIDs[0, 0]]):
    try:
        actualPic = [[None for _ in range(sideLen)] for _ in range(sideLen)]
        actualPic[0][0] = startingO
        for r in range(sideLen):
            for c in range(sideLen):
                if actualPic[r][c] is not None:  # just to handle (0, 0)
                    continue
                thisTile = tiles[picIDs[r][c]]
                filledAlr = [p for p in neighbors(sideLen, r, c) if actualPic[p[0]][p[1]] is not None].pop()
                tile = actualPic[filledAlr[0]][filledAlr[1]]
                if filledAlr[0] != r:  # it's upwards
                    matchUp = tile[-1]
                    for o in orientations(thisTile):
                        if o[0] == matchUp:
                            actualPic[r][c] = o
                            break

                else:  # it's to the left of the thing
                    matchUp = ''.join(r[-1] for r in tile)
                    for o in orientations(thisTile):
                        if ''.join(r[0] for r in o) == matchUp:
                            actualPic[r][c] = o
                            break
        break  # wow, everything matched up!
    except IndexError:  # well, that starting orientation wasn't valid, let's try another
        pass

final = []
for bigR in actualPic:
    for i in range(1, len(bigR[0]) - 1):  # exclude the top & bottom borders
        final.append(''.join(r[i][1:-1] for r in bigR))

nessie = [
    "..................#.",  # the ending dots are so the bodyLen is consistent
    "#....##....##....###",
    ".#..#..#..#..#..#..."
]
bodyLen = len(nessie[0])
for o in orientations(final):
    partOfNessie = np.zeros((len(final), len(final[0])))
    nessieCount = 0
    for i in range(len(final) - len(nessie) + 1):
        for s in range(len(o[0]) - bodyLen + 1):
            for v, r in enumerate(o[i:i + len(nessie)]):
                r = r[s: s + bodyLen]
                if re.match(nessie[v], r) is None:
                    break
            else:
                for v1 in range(len(nessie)):
                    for v2 in range(bodyLen):
                        partOfNessie[i + v1][s + v2] = nessie[v1][v2] == '#'
                nessieCount += 1
    if nessieCount:  # let's assume there's only ONE valid orientation
        final = o
        break

rough = 0
for r in range(len(final)):
    for c in range(len(final[0])):
        rough += not partOfNessie[r][c] and final[r][c] == '#'
print("i can't believe this took 200 lines of code: %i" % rough)
