from copy import deepcopy

lightStates = {}
justPoints = set()
with open('maybeDiamond.txt') as read:
    for y, line in enumerate(read):
        for x, c in enumerate(line.rstrip()):
            lightStates[(x, y)] = c == '#'  # True is on, False is off
            justPoints.add((x, y))

def lightNeighbors(pt):
    possibleNeighbors = {
        (pt[0] - 1, pt[1]), (pt[0] + 1, pt[1]), (pt[0], pt[1] - 1), (pt[0], pt[1] + 1),
        (pt[0] + 1, pt[1] + 1), (pt[0] - 1, pt[1] + 1), (pt[0] + 1, pt[1] - 1), (pt[0] - 1, pt[1] - 1)
    }
    return possibleNeighbors.intersection(justPoints)

partOneLights = deepcopy(lightStates)
for _ in range(100):
    newSetup = {}
    for l in partOneLights:
        neighborsOn = 0
        for n in lightNeighbors(l):
            if partOneLights[n]:
                neighborsOn += 1
        if not partOneLights[l] and neighborsOn == 3:
            newSetup[l] = True
        elif partOneLights[l] and neighborsOn not in [2, 3]:
            newSetup[l] = False
    partOneLights.update(newSetup)

print("again, the heck's my electric bill gonna be after this:%i" % len([p for p in partOneLights if partOneLights[p]]))

partTwoLights = deepcopy(lightStates)
endPX = max([x[0] for x in lightStates])
endPY = max([x[1] for x in lightStates])  # makes the program a bit more flexible
for l in lightStates:  # set all corners to on
    if l in [(0, 0), (0, endPY), (endPX, 0), (endPX, endPY)]:
        partTwoLights[l] = True

for _ in range(100):
    newSetup = {}
    for l in partTwoLights:
        if l in [(0, 0), (0, endPY), (endPX, 0), (endPX, endPY)]:
            continue  # don't even care, just leave it on like it is
        neighborsOn = 0
        for n in lightNeighbors(l):
            if partTwoLights[n]:
                neighborsOn += 1
        if not partTwoLights[l] and neighborsOn == 3:
            newSetup[l] = True
        elif partTwoLights[l] and neighborsOn not in [2, 3]:
            newSetup[l] = False
    partTwoLights.update(newSetup)

print("or maybe santa installed a hydro dam in my house:%i" % len([p for p in partTwoLights if partTwoLights[p]]))
