from dumbMazes.iHateMazes import findNeighbors

totalCoo = []
cooCheck = set()

with open('redditGood.txt') as bugs:
    yVal = 0
    for line in bugs.readlines():
        xVal = 0
        for c in line.rstrip():
            totalCoo.append([xVal, yVal, c == '#'])
            xVal += 1
        yVal += 1

for coo in totalCoo:
    allNeighbors = [[coo[0], coo[1]],
                    [coo[0], coo[1] + 1],
                    [coo[0] + 1, coo[1]],
                    [coo[0] - 1, coo[1]],
                    [coo[0], coo[1] - 1]]
    for p in allNeighbors:
        cooCheck.add(tuple(p))

for i in range(3):
    for coo in totalCoo:
        pass
