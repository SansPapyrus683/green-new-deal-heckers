from y2019.iHateIntcode.intcodeUtils import *


class Arcade(IntCode):
    def __init__(self, codeIn):
        super().__init__(codeIn)
        self.outputs = []
        self.scoreCount = 0
        self.calcScore = False

    def opThree(self, arg1):
        x = showBoard()
        self.data[arg1] = int(input("*atari intensifies* "))
        self.ballPos, self.boardPos = x[1][:2], x[2][:2]
        self.score = x[-1]
        self.v += 2
        self.data[arg1] = sign(self.ballPos[0] - self.boardPos[0])

    def opFour(self, arg1):
        self.outputs.append(arg1)
        self.v += 2


def showBoard():
    processed = []
    for chungus in chunks(code.outputs, 3):
        processed.append(chungus)
    xVals = list({a[0] for a in processed})
    yVals = list({a[1] for a in processed})
    xVals.sort()
    yVals.sort(reverse=True)
    canvas = [
        [x, y, False]
        for y in range(max(yVals) + 1)  # making a raw canvas
        for x in range(max(xVals) + 1)  # just consists of all the lightStates
    ]
    for p in processed:
        for pt in canvas:  # compares it with the outputs
            if p[:2] == pt[:2]:  # to see if it should be anything else
                canvas[canvas.index(pt)] = p
    result = []
    processed.reverse()
    for l in processed:
        if l[:2] == [-1, 0]:
            result.append(l[-1])
            print("Score: %s" % l[-1])
            break
    for chungus in chunks(canvas, max(xVals) + 1):
        temp = ""
        for pt in chungus:
            if pt[-1]:
                if pt[-1] == 1:
                    temp += " W "
                elif pt[-1] == 2:
                    temp += " B "
                elif pt[-1] == 3:
                    temp += "___"
                    result.append(pt)
                elif pt[-1] == 4:
                    temp += " * "
                    result.append(pt)
            else:
                temp += "   "

        print(temp)
    return result


# PART 1
with open("javaBad.txt") as stuff:
    Data = [int(x) for x in stuff.read().rstrip().split(sep=",")]
    code = Arcade(Data)
    code.interpret()
    blockCount = 0
    for chunk in chunks(code.outputs, 3):
        if chunk[-1] == 2:
            blockCount += 1
    print("Block count: %s" % blockCount)

# PART 2
code = Arcade(Data)
code.data[0] = 2
code.interpret()
print(code.score)
