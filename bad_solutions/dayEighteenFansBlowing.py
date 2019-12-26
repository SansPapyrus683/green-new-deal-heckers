"""neptune just reminds me of spongebob
WHO LIVES IN A PINEAPPLE UNDER THE SEA
maybe numpy would be good but heck that"""

def findNeighbors(pt: 'point', ptList: 'list of good points') -> 'list of neighbors':
    possibleNeighbors = [(pt[0] - 1, pt[1]), (pt[0] + 1, pt[1]), (pt[0], pt[1] - 1), (pt[0], pt[1] + 1)]
    goodNeighbors = []
    for p in possibleNeighbors:
        if p in ptList:
            goodNeighbors.append(p)
    return goodNeighbors

placesToGo = [] #itll be a list of tuples
keyLoc = []
assoDoorLoc = []

inFan = open('data stuff/test.txt')
with inFan as stuff:
    yVal = 0
    for l in reversed(stuff.readlines()):
        xVal = 0
        l = l.rstrip()
        for c in list(l):
            if c == '#':
                xVal += 1
            elif c == '.':
                placesToGo.append((xVal, yVal))
            elif c == '@':
                placesToGo.append((xVal, yVal))
                currPos = (xVal, yVal)
            else:
                placesToGo.append((xVal, yVal))
                if c.upper() == c: #door found
                    assoDoorLoc.append((xVal, yVal, c))
                else: #key instead
                    keyLoc.append((xVal, yVal, c))
            xVal += 1
        yVal += 1

#PART 1 OMG THIS IS WAY TOO LONG
totalMoves = 0
while True:
    moveCount = 0
    visited = [currPos]
    foundKey = False
    toBeProcessed = [currPos]
    while not foundKey:  #this loop goes until a key is found
        moveCount += 1
        inLine = []
        for p in toBeProcessed:
            goodPoints = [poi for poi in placesToGo if poi not in visited]
            inLine.extend(findNeighbors(p, goodPoints))
            visited.extend(findNeighbors(p, goodPoints))
        toBeProcessed = inLine[:]
        for k in keyLoc:
            if k[:-1] in toBeProcessed:
                keyFound = k[-1]
                keyLoc.remove(k)
                currPos = k[:-1]
                foundKey = True
                totalMoves += moveCount
                break

    if not keyLoc:
        break

    visited = [currPos]
    moveCount = 0
    foundDoor = False
    toBeProcessed = [currPos]
    while not foundDoor: #this loop goes until the door is found (from a key)
        moveCount += 1
        inLine = []
        for p in toBeProcessed:
            goodPoints = [poi for poi in placesToGo if poi not in visited]
            inLine.extend(findNeighbors(p, goodPoints))
            visited.extend(findNeighbors(p, goodPoints))
        toBeProcessed = inLine[:]
        for d in assoDoorLoc:
            if d[:-1] in toBeProcessed and d[-1] == keyFound.upper():
                assoDoorLoc.remove(d)
                currPos = d[:-1]
                foundDoor = True
                totalMoves += moveCount
                break

print('least amt of moves will take %i moves' % totalMoves)