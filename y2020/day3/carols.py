def treeNum(rMov, cMov, hills):
    start = (0, 0)  # row and column
    total = 0
    while start[0] + rMov < len(hills):
        start = (start[0] + rMov, (start[1] + cMov) % len(hills[0]))
        if hills[start[0]][start[1]] == '#':
            total += 1
    return total


with open('certifiedYuletide.txt') as read:
    bigHill = [line.rstrip() for line in read.readlines()]

print("these sled coordinates really got me tripping: %i" % treeNum(1, 3, bigHill))
treeProduct = 1
for r, c in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    treeProduct *= treeNum(r, c, bigHill)
print("but this was a pretty nice (if ez) puzzle overall: %i" % treeProduct)
