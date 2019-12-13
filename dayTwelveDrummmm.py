from itertools import combinations
from math import gcd
from sys import exit #for debugging

deathMoons = [
    {"x": -1, "y": 0, "z": 2},
    {"x": 2, "y": -10, "z": -7},
    {"x": 4, "y": -8, "z": 8},
    {"x": 3, "y": 5, "z": -1},
]
asoVelocities = [
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
]
# print(deathMoons)
stepCount = 0
while stepCount < 1000:
    for pair, pairAsoV in zip(
        combinations(deathMoons, 2), combinations(asoVelocities, 2)
    ):
        for c in ["x", "y", "z"]:
            if pair[0][c] > pair[1][c]:
                pairAsoV[0][c] -= 1
                pairAsoV[1][c] += 1
            elif pair[0][c] < pair[1][c]:
                pairAsoV[0][c] += 1
                pairAsoV[1][c] -= 1
    for v, p in enumerate(deathMoons):
        for k in p:
            p[k] += asoVelocities[v][k]
    # print('positions:',deathMoons)
    # print('velocities:', asoVelocities)
    # print('-' * 20)
    stepCount += 1

energySum = 0
for a, b in zip(deathMoons, asoVelocities):
    temp1, temp2 = 0, 0
    for k in a:
        temp1 += abs(a[k])
    for k in b:
        temp2 += abs(b[k])
    energySum += temp1 * temp2
print("the energy sum is %s" % energySum)


# PART 2
deathMoons = [
    {"x": -1, "y": 0, "z": 2},
    {"x": 2, "y": -10, "z": -7},
    {"x": 4, "y": -8, "z": 8},
    {"x": 3, "y": 5, "z": -1},
]
asoVelocities = [
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
]
def lcm(a, b):
    """shamelessly copied from stackoverlofw"""
    return abs(a * b) // gcd(a, b)


deathX = [[a["x"] for a in deathMoons]]
deathY = [[a["y"] for a in deathMoons]]
deathZ = [[a["z"] for a in deathMoons]]
deathX[0].extend([a["x"] for a in asoVelocities])
deathY[0].extend([a["y"] for a in asoVelocities])
deathZ[0].extend([a["z"] for a in asoVelocities])
def oneStep() -> list: #these two args specify the things needed
    for pair, pairAsoV in zip(
        combinations(deathMoons, 2), combinations(asoVelocities, 2)
    ):
        for c in ["x", "y", "z"]:
            if pair[0][c] > pair[1][c]:
                pairAsoV[0][c] -= 1
                pairAsoV[1][c] += 1
            elif pair[0][c] < pair[1][c]:
                pairAsoV[0][c] += 1
                pairAsoV[1][c] -= 1
    for v, p in enumerate(deathMoons):
        for k in p:
            p[k] += asoVelocities[v][k]
    return [[a['x'] for a in deathMoons] + [a['x'] for a in asoVelocities],
            [a['y'] for a in deathMoons] + [a['y'] for a in asoVelocities],
            [a['z'] for a in deathMoons] + [a['z'] for a in asoVelocities]]

for i in range(50):
    print(i, oneStep()[0])

exit()
cycles = []
axees = [deathX, deathY, deathZ]
while len(cycles) < 3:
    mark = 0
    for ax, l in zip(oneStep(), axees):
        if ax in l:
            print('found one for value %s' % l)
            cycles.append([len(l) - l.index(ax), [l.index(ax), len(l)]])
            axees.remove(l)
            break
        l.append(ax)
        mark += 1
print(cycles)