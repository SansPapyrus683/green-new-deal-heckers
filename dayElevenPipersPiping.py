from justStupidIntcode import intCode
from collections import defaultdict


class Robot(intCode):
    def __init__(self, code):
        self.data = code
        self.data = defaultdict(int)
        for v, i in enumerate(code):
            self.data[v] = i
        self.relBase = 0
        self.currPos = [0, 0]
        self.panels = [[0, 0]]
        self.asoColorings = [[0, False]]
        self.currOrientation = "up"
        self.count = 0

    def opThree(self, arg1):
        self.data[arg1] = self.asoColorings[self.panels.index(self.currPos)][0]
        self.v += 2
        # print('heres the value that was put into the robot : %s' %self.asoColorings[self.panels.index(self.currPos)])

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
        # print(' also heres the corresponding colors: %s' % self.asoColorings)
        self.v += 2


stuff = open("data stuff/peterPiper.txt")
with stuff as data:
    Data = [int(x) for x in data.readline().rstrip().split(sep=",")]
print(Data)
code = Robot(Data)
code.interpret()
sumPaints = 0
for panel in code.asoColorings:
    if panel[1]:
        sumPaints += 1
print(sumPaints)

# PART 2
def chunks(lst, n):
    """Yield successive n-sized chunks from lst. shamless copied from
    stack overflow lol"""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


code = Robot(Data)
code.asoColorings = [[1, False]]
code.interpret()
# print(code.asoColorings)
whitePanels = [
    x for x in code.panels if code.asoColorings[code.panels.index(x)][0] == 1
]
# print(whitePanels)
xVals = list({a[0] for a in code.panels})
yVals = list({a[1] for a in code.panels})
xVals.sort()
yVals.sort(reverse=True)
canvas = [
    [x, y, False]
    for x in range(min(xVals), max(xVals) + 1)
    for y in range(min(yVals), max(yVals) + 1)
]
for pt in canvas:
    if pt[:2] in whitePanels:
        pt[-1] = True
goodCanvs = []
for y in yVals:
    for c in canvas:
        if c[1] == y:
            goodCanvs.append(c)

for chungus in chunks(goodCanvs, max(xVals) - min(xVals) + 1):
    for c in chungus:
        if c[-1]:
            print(" M ", end="")
        else:
            print("   ", end="")
    print("")
