"""
this is part 2
the two parts of this puzzle follow pretty much exactly
the same logic, so i don't think i have to comment this
"""
from itertools import product
from copy import deepcopy
import numpy as np

SIM_AMT = 6


def neighbors(x: int, y: int, z: int, w: int):
    theNeighbors = []
    for triplet in product(*([[1, -1, 0]] * 4)):
        theNeighbors.append([x + triplet[0], y + triplet[1], z + triplet[2], w + triplet[3]])
    theNeighbors.remove([x, y, z, w])
    return theNeighbors


# NOTE: indices are referred to in w, z, y, x, not x, y, z, w because of array stuff
with open('manyWays.txt') as read:
    plane = [[int(i == '#') for i in line.rstrip()] for line in read.readlines()]
    assert len(plane) == len(plane[0]), 'can you just give a square as input?'
    arr = np.zeros((1, 1, len(plane), len(plane)))
    arr[0][0] = plane

for _ in range(SIM_AMT):
    wAndZ = len(arr) + 2
    xAndY = len(arr[0][0]) + 2
    expanded = np.zeros((wAndZ, wAndZ, xAndY, xAndY))
    expanded[1:wAndZ - 1, 1:wAndZ - 1, 1:xAndY - 1, 1:xAndY - 1] = arr
    arr = expanded

    newArr = deepcopy(arr)
    for x in range(xAndY):
        for y in range(xAndY):
            for z in range(wAndZ):
                for w in range(wAndZ):
                    filledCount = 0
                    for nX, nY, nZ, nW in neighbors(x, y, z, w):
                        if 0 <= nX < xAndY and 0 <= nY < xAndY and 0 <= nZ < wAndZ and 0 <= nW < wAndZ:
                            filledCount += arr[nW, nZ, nY, nX]
                    if arr[w, z, y, x] == 1 and filledCount not in [2, 3]:
                        newArr[w, z, y, x] = 0
                    elif arr[w, z, y, x] == 0 and filledCount == 3:
                        newArr[w, z, y, x] = 1
    arr = newArr

print("bro the protag has goddamn ascended to a new level of existence: %i" % np.sum(arr))
