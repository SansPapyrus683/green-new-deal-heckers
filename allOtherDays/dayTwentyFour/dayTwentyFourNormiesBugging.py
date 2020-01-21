from dumbMazes.iHateMazes import findNeighbors

totalCoo = []
cooCheck = {}

with open('redditGood.txt') as bugs:
    yVal = 0
    for line in bugs.readlines():
        xVal = 0
        for c in line.rstrip():
            totalCoo.append([xVal, yVal, c == '#'])
            xVal += 1
        yVal += 1

for coo in totalCoo:
    if not len(findNeighbors(tuple(coo[:-1]), {tuple(c[:-1]) for c in totalCoo})) == 4:
        print(coo)
        pass  # extend the cooCheck by some stuff

for i in range(3):
    for coo in totalCoo:
        pass
