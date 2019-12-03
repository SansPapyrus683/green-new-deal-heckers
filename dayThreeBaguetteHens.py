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
for prod in product(firstWireLines, secondWireLines):
    if prod[0][0][1] == prod[0][1][1] and prod[1][0][1] == prod[1][1][1]:
        pass
        #two vertical lines
    elif prod[0][0][0] == prod[0][1][0] and prod[1][0][0] == prod[1][1][0]:
        pass
        #two horizontal lines
    else:
        pass #a vertical and a horizonal
    print(prod)