"""what's funny is that i'm doing this during march rn (beer virus outbreak)"""
from collections import defaultdict

rowReq = 3010
columnReq = 3019
paper = defaultdict(lambda: defaultdict(lambda: 0))
paper[1][1] = 20151125
def findNext(row, column):
    tentativeNext = (row - 1, column + 1)
    if tentativeNext[0] == 0:
        return column + 1, 1
    return tentativeNext

before = [1, 1]
current = [2, 1]
while paper[rowReq][columnReq] == 0:
    paper[current[0]][current[1]] = (paper[before[0]][before[1]] * 252533) % 33554393
    before = current
    current = findNext(current[0], current[1])

print('there might be some way to optimize this but idc: %i' % paper[rowReq][columnReq])
print('if you see this, thanks 4 checking out my repo bro')
