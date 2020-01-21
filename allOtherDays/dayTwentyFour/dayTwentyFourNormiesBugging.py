totalCoo = []

with open('redditGood.txt') as bugs:
    yVal = 0
    for line in bugs.readlines():
        xVal = 0
        for c in line.rstrip():
            totalCoo.append([xVal, yVal, c == '#'])
            xVal += 1
        yVal += 1

for i in range(3):
    for coo in totalCoo:
        pass
