codeCount = 0
stringCount = 0
with open('checkOff.txt') as read:  # PART 1
    for line in read.readlines():
        line = line.rstrip()
        stringCount += len(eval(line))
        codeCount += len(line)

print('how much memory does santa\'s sleigh have anyways? %i' % (codeCount - stringCount))

encodedCount = 0
with open('checkOff.txt') as read:  # PART 2
    for line in read.readlines():
        for v, c in enumerate(line.rstrip()):
            if v not in [0, len(line.rstrip()) - 1] and c in ["\\", '"', "'", '']:
                encodedCount += 1
            encodedCount += 1
        encodedCount += 4  # for the surrounding quotes

print('a commodore 64 could probs store the input file lol: %i' % (encodedCount - codeCount))
