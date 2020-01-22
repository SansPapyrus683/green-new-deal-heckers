from dumbMazes.iHateMazes import findNeighbors

totalCoo = {}

with open('redditGood.txt') as bugs:
    yVal = 0
    for line in bugs.readlines():
        xVal = 0
        for c in line.rstrip():
            totalCoo[(xVal, yVal)] = c == '#'
            xVal += 1
        yVal += 1
borderValues = (max(p[0] for p in totalCoo),
                max(p[1] for p in totalCoo),
                min(p[0] for p in totalCoo),   # this is the values of all the border points or smth like that
                min(p[1] for p in totalCoo))


def borderCheck(pt):
    if pt[0] in borderValues or pt[1] in borderValues:
        return True
    return False


for i in range(1):
    for coo in totalCoo:
        neighborBugCount = 0
        if borderCheck(coo):
            pass  # do smth for the pts on the border
        else:
            neighbors = ([coo[0] + 1, coo[1]],
                         [coo[0] - 1, coo[1]],
                         [coo[0], coo[1] - 1],
                         [coo[0], coo[1] + 1])
            for pt in neighbors:
                if totalCoo[pt]:
                    neighborBugCount += 1
                    