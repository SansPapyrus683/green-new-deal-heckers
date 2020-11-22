from dumbMazes.iHateMazes import findNeighbors

# part 1, part 2 in separate file
# idk why it just seems to make it more organized

totalCoo = {}
borderPts = set()

with open('redditGood.txt') as bugs:
    yVal = 0
    for line in bugs.readlines():
        xVal = 0
        for c in line.rstrip():
            totalCoo[(xVal, yVal)] = c == '#'
            xVal += 1
        yVal += 1

for coo in totalCoo:
    regardlessNeighbors = [(coo[0] + 1, coo[1]), (coo[0] - 1, coo[1]), (coo[0], coo[1] - 1), (coo[0], coo[1] + 1)]
    for pt in regardlessNeighbors:
        if pt not in totalCoo:
            borderPts.add(pt)
for pt in borderPts:
    totalCoo[pt] = False

records = set()
while tuple(totalCoo.items()) not in records:
    records.add(tuple(totalCoo.items()))  # dicts aren't hashable so here
    newGrid = {}
    for coo in totalCoo:
        if coo in borderPts:
            continue  # move along now, you're a border point so you shouldn't be calculated
        neighborBugCount = 0
        for pt in findNeighbors(coo, set(totalCoo.keys())):
            if totalCoo[pt]:
                neighborBugCount += 1
        if totalCoo[coo]:  # tests if the bug has died or not
            if not neighborBugCount == 1:
                newGrid[coo] = False
        else:  # calculates if the space should be infected or not
            if neighborBugCount in [1, 2]:
                newGrid[coo] = True
    totalCoo.update(newGrid)

bioRating = 0
for pt in totalCoo:
    if totalCoo[pt]:
        bioRating += pow(2, 5 * pt[1] + pt[0])
print('i don\'t think this is how biology works but here\'s the rating anyways: %i' % bioRating)
