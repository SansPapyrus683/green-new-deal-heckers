from collections import defaultdict

housePresents = defaultdict(lambda: 0)  # by default the starting house has a present
housePresents[(0, 0)] += 1
currPos = [0, 0]

# PART 1
with open('noFire.txt') as read:
    for c in read.read().rstrip():
        if c == '>':
            currPos[0] += 1
        elif c == '^':
            currPos[1] += 1
        elif c == 'v':
            currPos[1] -= 1
        elif c == '<':
            currPos[0] -= 1
        housePresents[tuple(currPos)] += 1

print(len(housePresents), ' santa has terrible management')

# PART 2- data needs to be reset
housePresents = defaultdict(lambda: 0)
housePresents[(0, 0)] += 2
santa = [0, 0]
robot = [0, 0]

with open('noFire.txt') as read:
    for v, c in enumerate(read.read().rstrip()):
        if v % 2:  # robo-santa's turn
            if c == '>':
                robot[0] += 1
            elif c == '^':
                robot[1] += 1
            elif c == 'v':
                robot[1] -= 1
            elif c == '<':
                robot[0] -= 1
            housePresents[tuple(robot)] += 1
        else:
            if c == '>':
                santa[0] += 1
            elif c == '^':
                santa[1] += 1
            elif c == 'v':
                santa[1] -= 1
            elif c == '<':
                santa[0] -= 1
            housePresents[tuple(santa)] += 1

print(len(housePresents), ' i could do a better job and im 14 gosh darn it')
