r"""
boy do i love stackoverflow
https://stackoverflow.com/questions/11373122/best-way-to-store-a-triangular-hexagonal-grid-in-python
i actually rotated the coordinate system by 90 degrees
  _____       _____      ____      __
  / -2,2\_____/ 0,1 \____/2,0 \____/  \__
  \_____/-1,1 \_____/ 1,0\____/3,-1\__/
  /-2,1 \_____/0,0  \____/2,-1\____/  \__
  \_____/-1,0 \_____/1,-1\____/3,-2\__/
  /-2,0 \_____/ 0,-1\____/2,-2\____/  \__
  \_____/     \_____/    \____/    \__/    because as you can see this isn't oriented the right way for the problem
"""
from collections import defaultdict


def neighbors(p):
    return [
        (p[0], p[1] + 1),
        (p[0] + 1, p[1]),
        (p[0] + 1, p[1] - 1),
        (p[0], p[1] - 1),
        (p[0] - 1, p[1]),
        (p[0] - 1, p[1] + 1)
    ]


instructions = []
valid = {'e', 'se', 'sw', 'w', 'nw', 'ne'}
with open('manyTimesManyWays.txt') as read:
    for line in read.readlines():
        stepSeq = []
        line = line.strip().lower()
        i = 0
        while i < len(line):
            if i < len(line) - 1 and line[i:i+2] in valid:
                stepSeq.append(line[i:i+2])
                i += 1
            else:
                stepSeq.append(line[i])
            i += 1
        instructions.append(stepSeq)

tiles = defaultdict(lambda: True)  # all tiles start at True, or white
for i in instructions:
    pos = [0, 0]
    for s in i:
        if s == 'e':
            pos[1] += 1
        elif s == 'se':
            pos[0] += 1
        elif s == 'sw':
            pos[0] += 1
            pos[1] -= 1
        elif s == 'w':
            pos[1] -= 1
        elif s == 'nw':
            pos[0] -= 1
        elif s == 'ne':
            pos[0] -= 1
            pos[1] += 1
    pos = tuple(pos)
    tiles[pos] = not tiles[pos]
print("boy is this a crappy hotel: %i" % list(tiles.values()).count(False))

for _ in range(100):
    blackCounts = defaultdict(int)
    for t, color in tiles.items():
        blackCounts[t] = 0  # we have to set the tile itself, remember that lol
        for n in neighbors(t):
            blackCounts[n] += not color
    for t, count in blackCounts.items():
        if tiles[t] and count == 2:
            tiles[t] = False
        elif not tiles[t] and count == 0 or count > 2:
            tiles[t] = True
print("and how small are these tiles for goddamn %i to fit on the floor" % list(tiles.values()).count(False))
