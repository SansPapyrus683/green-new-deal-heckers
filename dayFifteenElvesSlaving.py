from justStupidIntcode import *
from sys import exit

# norht south east west 1 2 3 4 -> x + 1, x - 1, y+ 1, y - 1
# wall 0 (position hasnt changed), 1 empty, 2 oxygen
# right up left down or 3 1 2 4
class Droid(intCode):
    def __init__(self, code):
        super().__init__(code)
        self.coordinates = [[0, 0]] #good coordinates
        self.currPos = [0, 0]
        self.foundOx = False
        self.orientation = 1  # i kno this is the right hand rule but whatevs
        self.doneMoving = True
        self.moveCheck = 0 # but relly tho the above just goes through each of the moves

    def interpret(self):
        self.v = 0
        self.reference = self.data.copy()
        self.currSetting = 0
        while self.v <= len(self.data):
            # print(self.v, self.data[self.v])
            self.i = self.data[self.v]
            if str(self.i)[-2:] == "99":  # way too simple so i just included it in here
                break
            self.translator(self.i)
            if self.foundOx:
                break

        self.changed = self.data
        self.data = self.reference.copy()  # to change it back to the original

    def opThree(self, arg1):
        if self.doneMoving:
            # were done moving- now lets see the new thing
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
        # self.data[arg1] = int(input('hippity hoppity where do i go-ity '))
        self.orientation = self.data[arg1]
        self.v += 2

    def opFour(self, arg1):  # always just gives 0 1 or 2
        if arg1 == 0:  # this wall can commit not alive
            pass
            # print('dumb droid haha')
        elif arg1 == 1:  # well we moved
            self.move()
            if self.currPos not in self.coordinates:
                self.coordinates.append(self.currPos[:])
            # print(self.currPos)
            # self.showMaze()
            self.doneMoving = True
            self.moveCheck = 0
        elif arg1 == 2:  # HALLELUJAH
            self.move()
            if self.currPos not in self.coordinates:
                self.coordinates.append(self.currPos[:])
            self.foundOx = True
            self.oxSys = self.currPos[:]
            print("FOUND AT %s HALLELUJAH BABY" % self.currPos)
        # print(self.coordinates[-1])
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
            [x, y, False]
            for y in range(min(yVals), max(yVals) + 1)  # making a raw canvas
            for x in range(
                min(xVals), max(xVals) + 1
            )  # just consists of all the points
        ]
        for p in code.coordinates:
            for pt in canvas:
                if pt[:2] == p[:2]:
                    canvas[canvas.index(pt)] = p + [True]
        goodCanvas = list(chunks(canvas, max(xVals) - min(xVals) + 1))
        # print(goodCanvas)
        for chungus in reversed(goodCanvas):
            temp = ""
            for c in chungus:
                if c[-1]:
                    temp += " O "
                else:
                    temp += "   "
            print(temp)


with open("data stuff/amazonElves.txt") as stuff:
    Data = [int(x) for x in stuff.readline().rstrip().split(sep=",")]

# PART 1
code = Droid(Data)
code.interpret()
goodCoordinates = code.coordinates[:]
oxSys = code.oxSys[:]
toBeProcessed = [[0,0]] #some guy just told me to do bfs
moveCount = 0
while True: #theres probably a better way to do this
    processedNowDie = []
    inLine = []
    for v, p in enumerate(toBeProcessed):
        possibleNeighbours = [[p[0] + 1, p[1]], [p[0] - 1, p[1]], [p[0], p[1] + 1], [p[0], p[1] - 1]]
        for pt in possibleNeighbours:
            if pt in goodCoordinates: #delete the point itself thats being processed or smth
                inLine.append(pt) #idk this WONT WORK
                goodCoordinates.remove(pt)
        processedNowDie.append(v)
        if p in goodCoordinates:
            goodCoordinates.remove(p)
        
    for target in reversed(processedNowDie): del toBeProcessed[target]
    toBeProcessed.extend(inLine)
    moveCount += 1
    if oxSys in toBeProcessed:
        print('itll take %i moves to do this' % moveCount)
        break

#PART 2
goodCoordinates = code.coordinates[:]
oxSys = code.oxSys[:]
toBeProcessed = [oxSys[:]]
moveCount = 0
#ya know what if you
while goodCoordinates:
    pass
print('itll take %s minutes for all oxygen to infiltrate our base' % moveCount)