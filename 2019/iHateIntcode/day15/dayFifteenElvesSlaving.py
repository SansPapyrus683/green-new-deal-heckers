import sys
sys.path.insert(1, 'C:\\Users\\kevin\\OneDrive\\Documents\\GitHub\\green-newGame-deal-heckers\\2019\\iHateIntcode')
from justStupidIntcode import *
from mazeFuncForFifteen import *


# north south east west 1 2 3 4 -> x + 1, x - 1, y+ 1, y - 1
# wall 0 (position hasn't changed), 1 empty, 2 oxygen
# right up left down or 3 1 2 4
class Droid(intCode):
    def __init__(self, codeIn):
        super().__init__(codeIn)
        self.reference = self.data.copy()
        self.currSetting = 0
        self.v = 0
        self.coordinates = [(0, 0)]  # good coordinates
        self.currPos = [0, 0]
        self.foundOx = False
        self.orientation = 1  # i kno this is the right hand rule but whatever
        self.doneMoving = True
        self.moveCheck = 0
        self.foundAll = False

    def interpret(self):
        while self.v <= len(self.data):
            # print(self.v, self.data[self.v])
            self.i = self.data[self.v]
            if str(self.i)[-2:] == "99":  # way too simple so i just included it in here
                break
            self.translator(self.i)
            if self.foundOx and self.foundAll:
                self.showMaze()
                break

        self.changed = self.data
        self.data = self.reference.copy()  # to change it back to the original

    def opThree(self, arg1):
        if self.doneMoving:
            # were done moving- now lets see the newGame thing
            if self.orientation == 1:
                self.moveList = [3, 1, 4, 2]
            elif self.orientation == 2:
                self.moveList = [4, 2, 3, 1]
            elif self.orientation == 3:
                self.moveList = [2, 3, 1, 4]
            elif self.orientation == 4:
                self.moveList = [1, 4, 2, 3]
            self.doneMoving = False
        self.data[arg1] = self.moveList[self.moveCheck]
        self.moveCheck += 1
        self.orientation = self.data[arg1]
        self.v += 2

    def opFour(self, arg1):  # always just gives 0 1 or 2
        if arg1 == 0:  # this wall can commit not alive
            pass
            # print('dumb droid haha')
        elif arg1 == 1:  # well we moved
            self.move()
            if self.currPos not in self.coordinates:
                self.coordinates.append(tuple(self.currPos[:]))
            if self.currPos == [0, 0]:
                print("i think we explored all of it?")
                self.complete = self.coordinates
                self.foundAll = True
            self.doneMoving = True
            self.moveCheck = 0
        elif arg1 == 2:  # HALLELUJAH
            self.move()
            if self.currPos not in self.coordinates:
                self.coordinates.append(tuple(self.currPos[:]))
            self.foundOx = True
            self.oxSys = tuple(self.currPos[:])
            print("FOUND AT %s HALLELUJAH BABY" % self.currPos)
        self.v += 2

    def move(self):
        if self.orientation == 1:
            self.currPos[1] += 1
        elif self.orientation == 2:
            self.currPos[1] -= 1
        elif self.orientation == 3:
            self.currPos[0] += 1
        elif self.orientation == 4:
            self.currPos[0] -= 1

    def showMaze(self):
        xVals = list({a[0] for a in self.coordinates})
        yVals = list({a[1] for a in self.coordinates})
        canvas = [
            (x, y, False)
            for y in range(min(yVals), max(yVals) + 1)
            for x in range(min(xVals), max(xVals) + 1)
        ]
        for p in code.coordinates:
            for pt in canvas:
                if pt[:2] == p[:2]:
                    canvas[canvas.index(pt)] = p + (True,)

        for chungus in reversed(list(chunks(canvas, max(xVals) - min(xVals) + 1))):
            temp = ""
            for c in chungus:
                if c[-1]:
                    temp += " O "
                else:
                    temp += "   "
            print(temp)


with open("amazonElves.txt") as stuff:
    Data = [int(x) for x in stuff.readline().rstrip().split(sep=",")]

# PART 1
code = Droid(Data)
code.interpret()
goodCoordinates = code.coordinates[:]
oxSys = code.oxSys[:]
print("it'll take %i moves to do this" % justDistance((0, 0), goodCoordinates, oxSys))

# PART 2
goodCoordinates = code.coordinates[:]
oxSys = code.oxSys[:]
moveCount = 0
goodCoordinates.remove(oxSys)
processedNowDie = [oxSys[:]]
while goodCoordinates:
    inLine = []
    for v, p in enumerate(processedNowDie):
        for pt in findNeighbors(p, goodCoordinates):
            inLine.append(pt)
            goodCoordinates.remove(pt)

    processedNowDie = inLine
    moveCount += 1

print("it'll take %s minutes for all oxygen to infiltrate our base" % (moveCount - 1))
# minus 1 because it took one more minute
