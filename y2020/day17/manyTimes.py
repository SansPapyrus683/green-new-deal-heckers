"""
so this is part 1
i first used python lists
then after i discovered the wonders of numpy within about 5 minutes
i cleaned this up with said numpy
"""
from itertools import product
from copy import deepcopy
import numpy as np

SIM_AMT = 6


def neighbors(x: int, y: int, z: int):
    theNeighbors = []
    for triplet in product(*([[1, -1, 0]] * 3)):
        theNeighbors.append([x + triplet[0], y + triplet[1], z + triplet[2]])
    theNeighbors.remove([x, y, z])
    return theNeighbors


# NOTE: indices are referred to in z, y, x, not x, y, z because of array stuff
with open('manyWays.txt') as read:
    plane = [[int(i == '#') for i in line.rstrip()] for line in read.readlines()]
    assert len(plane) == len(plane[0]), 'can you just give a square as input?'
    arr = np.zeros((1, len(plane), len(plane)))
    arr[0] = plane

for _ in range(SIM_AMT):
    newZ = len(arr) + 2
    xAndY = len(arr[0]) + 2
    expanded = np.zeros((newZ, xAndY, xAndY))
    expanded[1:newZ - 1, 1:xAndY - 1, 1:xAndY - 1] = arr  # copy the array into the middle of the new one
    arr = expanded

    newArr = deepcopy(arr)
    for x in range(xAndY):
        for y in range(xAndY):
            for z in range(newZ):
                filledCount = 0
                for nX, nY, nZ in neighbors(x, y, z):
                    if 0 <= nX < xAndY and 0 <= nY < xAndY and 0 <= nZ < newZ:
                        filledCount += arr[nZ, nY, nX]
                if arr[z, y, x] == 1 and filledCount not in [2, 3]:
                    newArr[z, y, x] = 0
                elif arr[z, y, x] == 0 and filledCount == 3:
                    newArr[z, y, x] = 1
    arr = newArr

print("the heck? i thought christmas would go on without me lol: %i" % np.sum(arr))
