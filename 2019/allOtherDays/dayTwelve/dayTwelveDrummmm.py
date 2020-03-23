from itertools import combinations
from math import gcd

deathMoons = [
    {"x": 17, "y": -12, "z": 13},
    {"x": 2, "y": 1, "z": 1},
    {"x": -1, "y": -17, "z": 7},
    {"x": 12, "y": -14, "z": 18},
]
asoVelocities = [
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
]
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
    {"x": 17, "y": -12, "z": 13},
    {"x": 2, "y": 1, "z": 1},
    {"x": -1, "y": -17, "z": 7},
    {"x": 12, "y": -14, "z": 18},
]
asoVelocities = [
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
    {"x": 0, "y": 0, "z": 0},
]


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


deathX, deathY, deathZ = (
    [a["x"] for a in deathMoons] + [a["x"] for a in asoVelocities],
    [a["y"] for a in deathMoons] + [a["y"] for a in asoVelocities],
    [a["z"] for a in deathMoons] + [a["z"] for a in asoVelocities],
)
reference = [deathX, deathY, deathZ]  # to see if its the same as the starting position


def oneStep() -> list:  # these two args specify the things needed
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
    return [
        [a["x"] for a in deathMoons] + [a["x"] for a in asoVelocities],
        [a["y"] for a in deathMoons] + [a["y"] for a in asoVelocities],
        [a["z"] for a in deathMoons] + [a["z"] for a in asoVelocities],
    ]


cycles = []
allAxis = [
    [a[c] for a in deathMoons] + [a[c] for a in asoVelocities] for c in ["x", "y", "z"]
]
mark = 0
for a in allAxis:
    found = False
    count = 0
    while not found:
        ax = oneStep()[mark]
        if ax == reference[mark]:
            found = True
            cycles.append(count + 1)
        else:
            count += 1
    mark += 1
    deathMoons = [
        {"x": 17, "y": -12, "z": 13},
        {"x": 2, "y": 1, "z": 1},
        {"x": -1, "y": -17, "z": 7},
        {"x": 12, "y": -14, "z": 18},
    ]
    asoVelocities = [
        {"x": 0, "y": 0, "z": 0},
        {"x": 0, "y": 0, "z": 0},
        {"x": 0, "y": 0, "z": 0},
        {"x": 0, "y": 0, "z": 0},
    ]
x = lcm(cycles[0], cycles[1])
x = lcm(cycles[2], lcm(cycles[0], cycles[1]))
print('darn it takes %i time steps to complete a complete cycle'% x)
