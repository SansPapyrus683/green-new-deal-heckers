from justStupidIntcode import *
from collections import defaultdict
from math import copysign


class Arcade(intCode):
    def __init__(self, code):
        self.data = code
        self.data = defaultdict(int)
        for v, i in enumerate(code):
            self.data[v] = i
        self.relBase = 0
        self.outputs = []
        self.scoreCount = 0
        self.calcScore = False

    def opThree(self, arg1):
        # self.data[arg1] = int(input("*atari intensifies* "))
        x = showBoard()
        self.ballPos, self.boardPos = x[0][:2], x[1][:2]
        self.v += 2
        print(
            "ball position and board position are %s and %s"
            % (self.ballPos, self.boardPos)
        )
        self.data[arg1] = copysign(1, self.ballPos[0] - self.boardPos[0])
        print(copysign(1, self.ballPos[0] - self.boardPos[0]))

    def opFour(self, arg1):
        # print(arg1)
        self.outputs.append(arg1)
        self.v += 2


def showBoard():
    procsessed = []
    for chungus in chunks(code.outputs, 3):
        procsessed.append(chungus)
    xVals = list({a[0] for a in procsessed})
    yVals = list({a[1] for a in procsessed})
    xVals.sort()
    yVals.sort(reverse=True)
    canvas = [
        [x, y, False]
        for x in range(max(xVals) + 1)  # making a raw canvas
        for y in range(max(yVals) + 1)  # just consists of all the points
    ]
    goodCanvs = []
    for y in range(max(yVals) + 1):
        for c in canvas:
            if c[1] == y:
                goodCanvs.append(c)  # makes the points in the order i want
    for p in procsessed:
        for pt in goodCanvs:  # compares it with the outputs
            if p[:2] == pt[:2]:  # to see if it should be anything else
                goodCanvs[goodCanvs.index(pt)] = p
    result = []
    for l in goodCanvs:
        if l[:2] == [-1, 0]:
            print("Score: %s" % l[-1])
            goodCanvs.remove(l)
    for chungus in chunks(goodCanvs, max(xVals) + 1):
        #print(chungus)
        for pt in chungus:
            if pt[-1]:
                if pt[-1] == 1:
                    print(" W ", end="")  # wall or smth
                elif pt[-1] == 2:
                    print(" B ", end="")  # block
                elif pt[-1] == 3:
                    print("___", end="")  # the paddle
                    result.append(pt)
                elif pt[-1] == 4:
                    print(" * ", end="")  # the one ball
                    result.append(pt)
            else:
                print("   ", end="")
        print("")
    return result


# PART 1
with open("data stuff/javaBad.txt") as stuff:
    Data = [int(x) for x in stuff.read().rstrip().split(sep=",")]
    code = Arcade(Data)
    code.interpret()
    blockCount = 0
    for chungus in chunks(code.outputs, 3):
        if chungus[-1] == 2:
            blockCount += 1
    print('Block count: %s' % blockCount)

# PART 2
code = Arcade(Data)
code.data[0] = 2
code.interpret()