#WARNING: THIS SOLUTION IS VEEEEEEERY SLOW. AND BY VERY I MEAN VERY. IT ALSO ONLY DOES PART ONE
tooLongSoHereItIsInASeperateFile = open('frenchHens.txt')
#tooLongSoHereItIsInASeperateFile = open('test.txt')
for v, line in enumerate(tooLongSoHereItIsInASeperateFile):
    if v == 0:
        firstData = [s for s in line.rstrip().split(sep = ',')]
    elif v == 1:
        secondData = [s for s in line.rstrip().split(sep = ',')]
#above processes data basically
firstWireCoo, secondWireCoo = [], []
def pointArray(things, arrayAppend): #generates list of all points that the wires go through and appends them to arrayAppend
    currPos = [0,0]
    for s in things:
        #print(s, s[0])
        if s[0] == 'R':
            previousPos = currPos.copy()
            currPos[0] += int(s[1:])
            for i in range(int(s[1:]) + 1):
                arrayAppend.append([previousPos[0] + i, previousPos[1]])
        if s[0] == 'U':
            previousPos = currPos.copy()
            currPos[1] += int(s[1:])
            for i in range(int(s[1:]) + 1):
                arrayAppend.append([previousPos[0], previousPos[1] + i])
        if s[0] == 'L':
            previousPos = currPos.copy()
            currPos[0] -= int(s[1:])
            #print(previousPos, currPos)
            for i in range(currPos[0], previousPos[0] + 1):
                #print(i)
                arrayAppend.append([i, previousPos[1]])
        if s[0] == 'D':
            previousPos = currPos.copy()
            currPos[1] -= int(s[1:])
            for i in range(currPos[1], previousPos[1] + 1):
                #print(i)
                arrayAppend.append([previousPos[0], i])
pointArray(firstData, firstWireCoo)
pointArray(secondData, secondWireCoo)
middleman = []
for l in firstWireCoo:
    if not l in middleman:
        middleman.append(l)
firstWireCoo = middleman; middleman = []
for l in secondWireCoo: #removes all duplicates, these two for loops
    if not l in middleman:
        middleman.append(l)
goodPoints = []
for l in firstWireCoo:
    if l in secondWireCoo:
        goodPoints.append(l)
        #print('appended')
for l in secondWireCoo: #these two for loops just do the intersection (i cant use sets cuz u cant put lists in a set)
    if l in firstWireCoo and not l in goodPoints:
        goodPoints.append(l)
        #print('appended')
del goodPoints[0]
for v, thing in enumerate(goodPoints): #calculates manhattan distance of smth
    if v == 0:
        lowestScore = abs(thing[0]) + abs(thing[1])
    else:
        if abs(thing[0]) + abs(thing[1]) < lowestScore:
            lowestScore = abs(thing[0]) + abs(thing[1])
print(lowestScore)