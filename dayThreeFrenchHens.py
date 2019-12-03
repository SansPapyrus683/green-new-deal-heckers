tooLongSoHereItIsInASeperateFile = open('frenchHens.txt')
tooLongSoHereItIsInASeperateFile = open('test.txt')
for v, line in enumerate(tooLongSoHereItIsInASeperateFile):
    if v == 0:
        firstData = [s for s in line.rstrip().split(sep = ',')]
    elif v == 1:
        secondData = [s for s in line.rstrip().split(sep = ',')]

firstWireCoo, secondWireCoo = [], []
currPos = [0,0] #could also be startPos (the main CPU or smth idk)
for s in firstData:
    #print(s, s[0])
    if s[0] == 'R':
        previousPos = currPos.copy()
        currPos[0] += int(s[1:])
        for i in range(int(s[1:]) + 1):
            firstWireCoo.append([previousPos[0] + i, previousPos[1]])
    if s[0] == 'U':
        previousPos = currPos.copy()
        currPos[1] += int(s[1:])
        for i in range(int(s[1:]) + 1):
            firstWireCoo.append([previousPos[0], previousPos[1] + i])
    if s[0] == 'L':
        previousPos = currPos.copy()
        currPos[0] -= int(s[1:])
        print(previousPos, currPos)
        for i in range(currPos[0], previousPos[0] + 1):
            print(i)
            firstWireCoo.append([i, previousPos[1]])
    if s[0] == 'D':
        previousPos = currPos.copy()
        currPos[1] -= int(s[1:])
        for i in range(currPos[1], previousPos[1] + 1):
            print(i)
            firstWireCoo.append([previousPos[0], i])
print(firstWireCoo)