from functools import lru_cache


@lru_cache(None)  # this thing is fricking WONDERFUL
def p1Neighbors(row, col, rMax, cMax):
    return [p for p in [
        [row + 1, col], [row - 1, col], 
        [row, col + 1], [row, col - 1], 
        [row + 1, col + 1], [row + 1, col - 1], 
        [row - 1, col - 1], [row - 1, col + 1]
        ] if 0 <= p[0] < rMax and 0 <= p[1] < cMax]


@lru_cache(None)
def p2Neighbors(row, col, rMax, cMax, seats):
    neighborFuncs = [
        lambda x, y: [x + 1, y],
        lambda x, y: [x - 1, y],
        lambda x, y: [x, y - 1],
        lambda x, y: [x, y + 1],
        lambda x, y: [x + 1, y + 1],
        lambda x, y: [x + 1, y - 1],
        lambda x, y: [x - 1, y + 1],
        lambda x, y: [x - 1, y - 1],
    ]
    neighborPos = []
    for f in neighborFuncs:
        at = f(row, col)
        if not (0 <= at[0] < rMax and 0 <= at[1] < cMax):
            continue

        while seats[at[0]][at[1]] == '.':
            at = f(at[0], at[1])
            if not (0 <= at[0] < rMax and 0 <= at[1] < cMax):
                break
        else:
            neighborPos.append(at)
    return neighborPos



with open('onSleigh.txt') as read:
    seats = [line.rstrip() for line in read.readlines()]
backupSeats = seats.copy()

maxR = len(seats)
maxC = len(seats[0])

while True:
    newSeats = []
    for r in range(maxR):
        newRow = ''
        for c in range(maxC):
            neighbors = p1Neighbors(r, c, maxR, maxC)
            if seats[r][c] == 'L' and \
                all(seats[i][j] != '#' for i, j in neighbors):
                newRow += '#'
            elif seats[r][c] == '#' and \
                sum(seats[i][j] == '#' for i, j in neighbors) >= 4:
                newRow += 'L'
            else:
                newRow += seats[r][c]
        newSeats.append(newRow)
    if newSeats == seats:
        seats = newSeats
        break
    seats = newSeats
print("this ran slower than expected, oof: %i" % sum(r.count('#') for r in seats))

seats = backupSeats  # reset for part 2
tupledSeats = tuple(seats)
while True:
    newSeats = []
    for r in range(maxR):
        newRow = ''
        for c in range(maxC):
            neighbors = p2Neighbors(r, c, maxR, maxC, tupledSeats)
            if seats[r][c] == 'L' and \
                all(seats[i][j] != '#' for i, j in neighbors):
                newRow += '#'
            elif seats[r][c] == '#' and \
                sum(seats[i][j] == '#' for i, j in neighbors) >= 5:
                newRow += 'L'
            else:
                newRow += seats[r][c]
        newSeats.append(newRow)
    if newSeats == seats:
        seats = newSeats
        break
    seats = newSeats
print("don't you hate it when you have too segments "
      "that are so similar but just different enough so that "
      "they can't be made into a function: %i" % sum(r.count('#') for r in seats))
