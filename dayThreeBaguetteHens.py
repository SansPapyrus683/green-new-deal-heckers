#a better one that only calculates line segments
from itertools import product
tooLongSoHereItIsInASeperateFile = open('frenchHens.txt')
tooLongSoHereItIsInASeperateFile = open('test.txt')
for v, line in enumerate(tooLongSoHereItIsInASeperateFile):
    if v == 0:
        firstData = [s for s in line.rstrip().split(sep = ',')]
    elif v == 1:
        secondData = [s for s in line.rstrip().split(sep = ',')]
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
goodLines = [] #the set of intersection points
for prod in product(firstWireLines, secondWireLines):
    if prod[0][0][1] == prod[0][1][1] and prod[1][0][1] == prod[1][1][1]:
        if prod[0][0][1] == prod[0][1][1] == prod[1][0][1] == prod[1][1][1]:
            firstRange = range(prod[0][0][0], prod[0][1][0])
            secondRange = range(prod[1][0][0], prod[1][1][0])
            setFirstRange = set(firstRange)
            for x in setFirstRange.intersection(secondRange):
                goodLines.append([x, prod[0][0][1]]) #you could use any prod[][][] or something
        #two horizontal lines
    elif prod[0][0][0] == prod[0][1][0] and prod[1][0][0] == prod[1][1][0]:
        if prod[0][0][0] == prod[0][1][0] == prod[1][0][0] == prod[1][1][0]:
            firstRange = range(prod[0][0][1], prod[0][1][1])
            secondRange = range(prod[1][0][1], prod[1][1][1])
            setFirstRange = set(firstRange)
            for x in setFirstRange.intersection(secondRange):
                goodLines.append([prod[0][0][0], x])
        #two vertical lines
    else:
        if (prod[0][0][0]-prod[1][0][0])*(prod[0][1][0]-prod[1][1][0]) <= 0 and (prod[0][0][1]-prod[1][0][1])*(prod[0][1][1]-prod[1][1][1]) <= 0:
            print('yeet')
            print(prod)
        #a vertical and a horizonal
print(goodLines)
#If you want to know if vertical and horizontal line segments cross, 
# you can do something like: 
# (point1_start_x - point2_start_x) * (point1_end_x - point2_end_x) <= 0 and (point1_start_y - point2_start_y) * (point1_end_y - point2_end_y) <= 0.