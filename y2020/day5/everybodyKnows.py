ROW_POW = 7
COL_POW = 3
with open('whatDoTheyKnow.txt') as read:
    boardingPasses = [[p[:ROW_POW], p[ROW_POW:ROW_POW + COL_POW].rstrip()] for p in read.readlines()]

seatIDs = []
for b in boardingPasses:
    rowLo = 0
    rowHi = 2 ** ROW_POW
    for i in b[0]:  # doing all that binary searching for usaco did help, neat
        if i == 'B':
            rowLo = (rowLo + rowHi) // 2
        elif i == 'F':
            rowHi = (rowLo + rowHi) // 2
        else:
            raise ValueError("wait are you sure your input's valid?")
    colLo = 0
    colHi = 2 ** COL_POW
    for i in b[1]:
        if i == 'R':
            colLo = (colLo + colHi) // 2
        elif i == 'L':
            colHi = (colLo + colHi) // 2
        else:
            raise ValueError("wait are you sure your input's valid?")
    seatIDs.append(rowLo * (ROW_POW + 1) + colLo)

print("wait lol it's day 5 and we're STILL on the plane? bruh... %i" % max(seatIDs))
for i in range(min(seatIDs) + 1, max(seatIDs)):  # get the lower and upper bound for all the seats
    if i not in seatIDs:
        print("wait aren't online boarding passes a thing? couldn't we've just looked there: %i" % i)
        break
