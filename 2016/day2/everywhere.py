instructions = []
with open('seriouslyEverywhere.txt') as read:
    for l in read:
        instructions.append(l.rstrip())

movement = {
    "U": lambda x, y: [x, y - 1],  # positive y actually goes down
    "D": lambda x, y: [x, y + 1],
    "L": lambda x, y: [x - 1, y],
    "R": lambda x, y: [x + 1, y]
}

# PART 1
code = ""
start = [1, 1]
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in instructions:
    for m in i:
        start = movement[m](start[0], start[1])
        start[0] = max(0, min(start[0], 2))  # stop from going out of bounds
        start[1] = max(0, min(start[1], 2))
    code += str(grid[start[1]][start[0]])
print("ok why does the bathroom have a lock it's not like it's a safe: %s" % code)

# PART 2
code = ""
start = [-2, 0]  # set the middle as 0, 0 this time
grid = {
    -2: {0: '5'},
    -1: {1: 'A', 0: '6', -1: '2'},
    0: {2: 'D', 1: 'B', 0: '7', -1: '3', -2:'1'},
    1: {1: 'C', 0: '8', -1: '4'},
    2: {0: '9'}
}
for i in instructions:
    for m in i:
        prevStart = start.copy()
        start = movement[m](start[0], start[1])
        if sum([abs(start[0]), abs(start[1])]) > 2:
            start = prevStart
    code += str(grid[start[0]][start[1]])  # this one is x then y bc it's not a matrix
print("this keypad is absolutely horrible: %s" % code)
