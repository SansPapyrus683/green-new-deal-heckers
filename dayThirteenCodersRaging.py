from justStupidIntcode import *
from collections import defaultdict


class Arcade(intCode):
    def __init__(self, code):
        self.data = code
        self.data = defaultdict(int)
        for v, i in enumerate(code):
            self.data[v] = i
        self.relBase = 0
        self.outputs = []

    def opFour(self, arg1):
        # print(arg1)
        self.outputs.append(arg1)
        self.v += 2


# PART 1
with open("data stuff/javaBad.txt") as stuff:
    Data = [int(x) for x in stuff.read().rstrip().split(sep=",")]
    code = Arcade(Data)
    code.interpret()
    blockCount = 0
    for v, i in enumerate(code.outputs):
        if (v - 2) % 3 == 0:
            if i == 2:
                blockCount += 1
    print("block count: %s" % blockCount)

# PART 2
code.data[0] = 2
procsessed = []
for chungus in chunks(code.outputs, 3):
    procsessed.append(chungus)
code.outputs = procsessed
del procsessed
xVals = list({a[0] for a in code.outputs})
yVals = list({a[1] for a in code.outputs})
xVals.sort()
yVals.sort(reverse=True)
canvas = [
    [x, y, False]
    for x in range(min(xVals), max(xVals) + 1)
    for y in range(min(yVals), max(yVals) + 1)
]
goodCanvs = []
for y in yVals:
    for c in canvas:
        if c[1] == y:
            goodCanvs.append(c)
#print(code.outputs)
for p in code.outputs:
    # print('pt: %s' % p)
    for pt in goodCanvs:
        if p[:2] == pt[:2]:
            # print(pt)
            goodCanvs[goodCanvs.index(pt)] = p
#print(goodCanvs)

for chungus in chunks(goodCanvs, max(xVals) - min(xVals) + 1):
    for pt in chungus:
        if pt[-1]:
            if pt[-1] == 1:
                print(" W ", end="")
            elif pt[-1] == 2:
                print(" B ", end="")
            elif pt[-1] == 3:
                print("___", end="")
            elif pt[-1] == 4:
                print(" * ", end="")
        else:
            print("   ", end="")
    print("")
