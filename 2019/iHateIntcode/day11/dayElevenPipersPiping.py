import sys
sys.path.insert(1, 'C:\\Users\\kevin\\OneDrive\\Documents\\GitHub\\green-newGame-deal-heckers\\2019\\iHateIntcode')
from justStupidIntcode import *


class Robot(intCode):
    def __init__(self, code):
        super().__init__(code)
        self.currPos = [0, 0]
        self.panels = [[0, 0]]
        self.asoColorings = [[0, False]]
        self.currOrientation = "up"
        self.count = 0

    def opThree(self, arg1):
        self.data[arg1] = self.asoColorings[self.panels.index(self.currPos)][0]
        self.v += 2

    def opFour(self, arg1):
        self.count += 1
        if self.count == 1:
            self.asoColorings[self.panels.index(self.currPos)] = [arg1, True]
            # print('the tile of %s was painted %s' %(self.currPos, arg1))
        elif self.count == 2:
            if self.currOrientation == "up":
                if arg1 == 0:
                    self.currOrientation = "left"
                    self.currPos[0] -= 1
                else:
                    self.currOrientation = "right"
                    self.currPos[0] += 1
            elif self.currOrientation == "down":
                if arg1 == 0:
                    self.currOrientation = "right"
                    self.currPos[0] += 1
                else:
                    self.currOrientation = "left"
                    self.currPos[0] -= 1
            elif self.currOrientation == "left":
                if arg1 == 0:
                    self.currOrientation = "down"
                    self.currPos[1] -= 1
                else:
                    self.currOrientation = "up"
                    self.currPos[1] += 1
            elif self.currOrientation == "right":
                if arg1 == 0:
                    self.currOrientation = "up"
                    self.currPos[1] += 1
                else:
                    self.currOrientation = "down"
                    self.currPos[1] -= 1
            self.count = 0
        if self.currPos not in self.panels:
            self.panels.append(self.currPos[:])
            self.asoColorings.append([0, False])
        # print('position and the argument that was outputted',self.currPos, arg1)
        # print('all the panels the robot has visited: %s' % self.panels)
        # print('also here\'s the corresponding colors and if they've been painted: %s' % self.asoColorings)
        self.v += 2


with open("peterPiper.txt") as data:
    Data = [int(x) for x in data.readline().rstrip().split(sep=",")]
    code = Robot(Data)

code.interpret()
sumPaints = 0
for panel in code.asoColorings:
    if panel[1]:
        sumPaints += 1
print(sumPaints, '<---- part 1 ans or smth')

# PART 2
code = Robot(Data)
code.asoColorings = [[1, False]]
code.interpret()
paintedPanels = [x for x in code.panels if code.asoColorings[code.panels.index(x)][0] == 1]
xVals = list({a[0] for a in code.panels})
yVals = list({a[1] for a in code.panels})
canvas = [
    [x, y, False]
    for y in range(min(yVals), max(yVals) + 1)
    for x in range(min(xVals), max(xVals) + 1)
]
for pt in canvas:
    if pt[:2] in paintedPanels:
        pt[-1] = True

canvas.reverse()
for smallChunk in chunks(canvas, max(xVals) - min(xVals) + 1):
    smallChunk.reverse()
    for c in smallChunk:
        if c[-1]:
            print(" # ", end="")
        else:
            print("   ", end="")
    print("")
