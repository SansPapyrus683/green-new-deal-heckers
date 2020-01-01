tooLongSoHereItIsInASeperateFile = open(
    "C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/frenchHens.txt"
)

for v, line in enumerate(tooLongSoHereItIsInASeperateFile):
    if v == 0:
        firstData = [s for s in line.rstrip().split(sep=",")]
    elif v == 1:
        secondData = [s for s in line.rstrip().split(sep=",")]

firstPts = set()
secondPts = set()


# PART 1
def makePts(lines, appendSet: set) -> set:
    initialPt = [0, 0]
    appendSet.add((0, 0))
    for l in lines:
        magnitude = int(l[1:])  # the amt that the movement instruction moved
        if l[0] == 'U':
            appendSet.update(
                [tuple([initialPt[0], initialPt[1] + i]) for i in range(magnitude)])
            initialPt[1] += magnitude
        elif l[0] == 'D':
            appendSet.update(
                [tuple([initialPt[0], initialPt[1] - i]) for i in range(magnitude)])
            initialPt[1] -= magnitude
        elif l[0] == 'L':
            appendSet.update(
                [tuple([initialPt[0] - i, initialPt[1]]) for i in range(magnitude)])
            initialPt[0] -= magnitude
        elif l[0] == 'R':
            appendSet.update(
                [tuple([initialPt[0] + i, initialPt[1]]) for i in range(magnitude)])
            initialPt[0] += magnitude


makePts(firstData, firstPts)
makePts(secondData, secondPts)
intersections = firstPts.intersection(secondPts)
intersections.remove((0, 0))

print(intersections)
lowestDistance = float('inf')
for cross in intersections:
    if abs(cross[0]) + abs(cross[1]) < lowestDistance:
        lowestDistance = sum(cross)

print(lowestDistance)


# PART 2
def makePts(command: str, currPos) -> tuple:
    magnitude = int(command[1:])
    if command[0] == 'U':
        return [tuple([currPos[0], currPos[1] + i]) for i in range(magnitude)], (currPos[0], currPos[1] + magnitude)
    elif command[0] == 'D':
        return [tuple([currPos[0], currPos[1] - i]) for i in range(magnitude)], (currPos[0], currPos[1] - magnitude)
    elif command[0] == 'L':
        return [tuple([currPos[0] - i, currPos[1]]) for i in range(magnitude)], (currPos[0] - magnitude, currPos[1])
    elif command[0] == 'R':
        return [tuple([currPos[0] + i, currPos[1]]) for i in range(magnitude)], (currPos[0] + magnitude, currPos[1])


lowestResistance = float('inf')
for pt in intersections:
    firstCount, secondCount = 0, 0
    initialPt = (0, 0)
    for com in firstData:
        traversed = makePts(com, initialPt)
        if pt in traversed[0]:
            firstCount += len(traversed[0][:traversed[0].index(pt)])
            break
        firstCount += len(traversed[0])
        initialPt = traversed[1]
    initialPt = (0, 0)
    for com in secondData:
        traversed = makePts(com, initialPt)
        if pt in traversed[0]:
            secondCount += len(traversed[0][:traversed[0].index(pt)])
            break
        secondCount += len(traversed[0])
        initialPt = traversed[1]

    if firstCount + secondCount < lowestResistance:
        lowestResistance = firstCount + secondCount

print(lowestResistance)