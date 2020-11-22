from collections import deque

operations = []
with open("neatToys.txt") as read:
    for l in read.readlines():
        operations.append(l.rstrip())

colNum = 50
rowNum = 6
grid = [[False for _ in range(colNum)] for _ in range(rowNum)]
for op in operations:
    if op.startswith("rect"):
        op = [int(d) for d in op[5:].split('x')]
        for r in range(op[1]):
            for c in range(op[0]):
                grid[r][c] = True

    elif op.startswith("rotate column"):
        op = [int(i) for i in op[16:].split(" by ")]  # 1st is index of the grid to operate on, 2nd is how much to
        opOn = deque([r[op[0]] for r in grid])
        opOn.rotate(op[1])
        for r, a in zip(grid, opOn):
            r[op[0]] = a

    elif op.startswith("rotate row"):
        op = [int(i) for i in op[13:].split(" by ")]
        opOn = deque(grid[op[0]])
        opOn.rotate(op[1])
        grid[op[0]] = list(opOn)

count = 0
for row in grid:
    for li in row:
        print('█' if li else ' ', end='')  # that's the scp redacted character lol
        count += 1 if li else 0
    print('')
print("you could count for yourself but lemme do it... let's see... yeah there's %s lit lights" % count)
