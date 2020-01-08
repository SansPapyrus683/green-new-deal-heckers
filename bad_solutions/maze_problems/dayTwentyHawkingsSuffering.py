validPlaces = []  # list of tuples, and empty places are in the coordinate system

with open('C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/test.txt') as data:
    yVal = 0
    mazeList = []
    for v, line in enumerate(data):
        mazeList.append(list(line.rstrip()))
        xVal = 0
        for c in line:
            if c == '.':
                validPlaces.append((xVal, yVal))
            xVal += 1
        yVal += 1

    conformLen = max([len(l) for l in mazeList])
    for line in mazeList:
        if len(line) < conformLen:
            line.extend([' ' for i in range(conformLen - len(line))])

    print(mazeList)
print(validPlaces)
