import os
os.chdir("2016/day1")

with open('doLookLikeChristmas.txt') as read:
    directions = read.read().rstrip().split(sep=', ')

visitedBefore = {(0, 0)}
gottenTwice = False
coordinates = [0, 0]
currOrientation = 'north'
rightPaths = {'north': 'east', 'east': 'south', 'south': 'west', 'west': 'north'}
leftPaths = {'north': 'west', 'west': 'south', 'south': 'east', 'east': 'north'}


def move(coo, facing, distance):
    global gottenTwice
    if facing == 'north':
        action = "coo[1] += 1"
    elif facing == 'south':
        action = "coo[1] -= 1"
    elif facing == 'east':
        action = "coo[0] += 1"
    elif facing == 'west':
        action = "coo[0] -= 1"

    for _ in range(distance):
        exec(action)
        if tuple(coo) in visitedBefore and not gottenTwice:
            print('bruh the protagonist is so dumb lol: %s' % sum([abs(i) for i in coo]))
            gottenTwice = True
        visitedBefore.add(tuple(coo))



for d in directions:
    if d[0] == 'R':
        currOrientation = rightPaths[currOrientation]
        move(coordinates, currOrientation, int(d[1:]))
    else:
        currOrientation = leftPaths[currOrientation]
        move(coordinates, currOrientation, int(d[1:]))

print('what kind of stupid directions are these: %i' % sum([abs(i) for i in coordinates]))  # part 1
