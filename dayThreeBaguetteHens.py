#a better one that only calculates line segments
from itertools import product
tooLongSoHereItIsInASeperateFile = open('frenchHens.txt')
#tooLongSoHereItIsInASeperateFile = open('test.txt')
for v, line in enumerate(tooLongSoHereItIsInASeperateFile):
    if v == 0:
        firstData = [s for s in line.rstrip().split(sep = ',')]
    elif v == 1:
        secondData = [s for s in line.rstrip().split(sep = ',')]
#PART 1 PEOPLE
firstWireLines, secondWireLines = [], []
def genLines(data, resultList):
    currPos = [0,0]
    for s in data:
        if s[0] == 'R':
            resultList.append([currPos, [currPos[0]+int(s[1:]), currPos[1]]])
            currPos = [currPos[0]+int(s[1:]), currPos[1]]
        elif s[0] == 'U':
            resultList.append([currPos, [currPos[0], currPos[1]+int(s[1:])]])
            currPos = [currPos[0], currPos[1]+int(s[1:])]
        elif s[0] == 'L':
            resultList.append([currPos, [currPos[0]-int(s[1:]), currPos[1]]])
            currPos = [currPos[0]-int(s[1:]), currPos[1]]
        elif s[0] == 'D':
            resultList.append([currPos, [currPos[0], currPos[1]-int(s[1:])]])
            currPos = [currPos[0], currPos[1]-int(s[1:])]

genLines(firstData, firstWireLines); genLines(secondData, secondWireLines)
print(firstWireLines, secondWireLines)
goodPoints = [] #the set of intersection points
associatedLines = [] #for part 2
for prod in product(firstWireLines, secondWireLines):
    copied = prod[:]
    for thing in copied: thing.sort()
    if copied[0][0][1] == copied[0][1][1] and copied[1][0][1] == copied[1][1][1]:
        if copied[0][0][1] == copied[0][1][1] == copied[1][0][1] == copied[1][1][1]:
            firstRange = range(copied[0][0][0], copied[0][1][0])
            secondRange = range(copied[1][0][0], copied[1][1][0])
            setFirstRange = set(firstRange)
            for x in setFirstRange.intersection(secondRange):
                goodPoints.append([x, copied[0][0][1]]) #you could use any copied[][][] or something
                associatedLines.append(copied)
        #two horizontal lines
    elif copied[0][0][0] == copied[0][1][0] and copied[1][0][0] == copied[1][1][0]:
        if copied[0][0][0] == copied[0][1][0] == copied[1][0][0] == copied[1][1][0]:
            firstRange = range(copied[0][0][1], copied[0][1][1])
            secondRange = range(copied[1][0][1], copied[1][1][1])
            setFirstRange = set(firstRange)
            for x in setFirstRange.intersection(secondRange):
                goodPoints.append([copied[0][0][0], x])
                associatedLines.append(copied)
        #two vertical lines
    else:
        if (copied[0][0][0]-copied[1][0][0])*(copied[0][1][0]-copied[1][1][0]) <= 0 and (copied[0][0][1]-copied[1][0][1])*(copied[0][1][1]-copied[1][1][1]) <= 0:
            # (point1_start_x - point2_start_x) * (point1_end_x - point2_end_x) <= 0 and (point1_start_y - point2_start_y) * (point1_end_y - point2_end_y) <= 0.
            if copied[0][0][1] == copied[0][1][1]:
                goodPoints.append([copied[1][0][0], copied[0][0][1]])
                associatedLines.append(copied)
            else:
                goodPoints.append([copied[0][0][0], copied[1][0][1]])
                associatedLines.append(copied)
            #print(copied)
        #a vertical and a horizonal
#print(goodPoints)
if [0,0] in goodPoints: 
    del associatedLines[goodPoints.index([0,0])]
    del goodPoints[goodPoints.index([0,0])]

for v, thing in enumerate(goodPoints): #calculates manhattan distance of smth
    if v == 0:
        lowestScore = abs(thing[0]) + abs(thing[1])
    else:
        if abs(thing[0]) + abs(thing[1]) < lowestScore:
            lowestScore = abs(thing[0]) + abs(thing[1])
#print(lowestScore)

#PART 2
lowestScore = 10000000000000000000000 #someone tell me if theres a better way to do this
print(associatedLines)
for v, point in enumerate(goodPoints):
    lines = associatedLines[v]
    print(point, lines)
    #print(lines[0])
    firstCount, secondCount = 0, 0
    for x in firstWireLines:
        if x == lines[0]:
            if x[0][0] == x[1][0]:
                firstCount += abs(point[1] - x[0][1])
                #print(abs(point[1] - x[1][1]))
            else:
                firstCount += abs(point[0] - x[0][0])
                #print(abs(point[0] - x[1][0]))
            break
        else:
            if x[0][0] == x[1][0]:
                firstCount += abs(x[0][1] - x[1][1])
            else:
                firstCount += abs(x[0][0] - x[1][0])
    for x in secondWireLines:
        if x == lines[1]:
            if x[0][0] == x[1][0]:
                secondCount += abs(point[1] - x[0][1])
                #print(abs(point[1] - x[1][1]))
            else:
                secondCount += abs(point[0] - x[0][0])
                #print(abs(point[0] - x[1][0]))
            break
        else:
            if x[0][0] == x[1][0]:
                secondCount += abs(x[0][1] - x[1][1])
            else:
                secondCount += abs(x[0][0] - x[1][0])
    if firstCount + secondCount < lowestScore: lowestScore = firstCount + secondCount
print(lowestScore)