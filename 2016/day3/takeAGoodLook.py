validCount = 0
with open('fiveAndTen.txt') as read:  # PART 1
    for line in read.readlines():
        line = [int(i) for i in line.rstrip().split()]
        if sum(line) - max(line) > max(line):
            validCount += 1

print('just did this to see what happens if you complete later days first: %i' % validCount)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]

validCountCol = 0  # i could put the two together but i think this is more readable
with open('fiveAndTen.txt') as read:  # PART 2
    triangles = []
    processed = []
    for line in read.readlines():
        processed.append([int(i) for i in line.rstrip().split()])
    for col in zip(*processed):
        for tri in chunks(col, 3):
            if sum(tri) - max(tri) > max(tri):
                validCountCol += 1
print('nothing out of the ordinary happened lol: %i' % validCountCol)
