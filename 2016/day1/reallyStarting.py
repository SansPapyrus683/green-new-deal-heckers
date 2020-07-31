with open('doLookLikeChristmas.txt') as read:
    directions = read.read().rstrip().split(sep=', ')

def move(coo, facing, distance):
    if facing == 'north':
        coo[1] += distance

    elif facing == 'south':
        coo[1] -= distance

    elif facing == 'east':
        coo[0] += distance

    elif facing == 'west':
        coo[0] -= distance

coordinates = [0, 0]
visitedBefore = [coordinates]
currOrientation = 'north'
rightPaths = {'north': 'east', 'east': 'south', 'south': 'west', 'west': 'north'}
leftPaths = {'north': 'west', 'west': 'south', 'south': 'east', 'east': 'north'}

first = True
for d in directions:
    prevCoo = coordinates.copy()  # TODO: this thing still hasn't been finished
    if d[0] == 'R':
        currOrientation = rightPaths[currOrientation]
        move(coordinates, currOrientation, int(d[1:]))
        if coordinates[0] != prevCoo[0]:
            pass  # move on x
        else:
            pass  # move on y

    else:
        currOrientation = leftPaths[currOrientation]
        move(coordinates, currOrientation, int(d[1:]))
        if coordinates[0] != prevCoo[0]:
            pass  # move on x
        else:
            pass  # move on y

    visitedBefore.append(coordinates)

print('what kind of stupid directions are these: %i' % abs(sum(coordinates)))  # part 1
