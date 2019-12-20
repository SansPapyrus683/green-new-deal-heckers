from justStupidIntcode import *
from sys import exit
#norht south east west 1 2 3 4 -> x + 1, x - 1, y+ 1, y - 1
#wall 0 (position hasnt changed), 1 empty, 2 oxygen
#right up left down or 3 1 2 4
class Droid(intCode):
    def __init__(self, code):
        super().__init__(code)
        self.coordinates = [[0,0]] #coordinates then thing
        #these coordinates only have valid positions
        self.currPos = [0, 0]
        self.foundOx = False
        self.orientation = 1 #i kno this is the right hand rule but whatevs
        self.doneMoving = True
        self.moveCheck = 0 #vibe check intensifies
        #but relly tho the above just goes through each of the moves

    def interpret(self):
        self.v = 0
        self.reference = self.data.copy()
        self.currSetting = 0
        while self.v <= len(self.data):
            #print(self.v, self.data[self.v])
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
        #were done moving- now lets see the new thing
            if self.orientation == 1:
                self.moveList = [3,1,4,2] #these stuff in wrong order, must fix
            elif self.orientation == 2:
                self.moveList = [4,2,3,1]
            elif self.orientation == 3:
                self.moveList = [2,3,1,4]
            elif self.orientation == 4:
                self.moveList = [1,4,2,3]
            self.doneMoving = False
        self.data[arg1] = self.moveList[self.moveCheck]
        self.moveCheck += 1
        #self.data[arg1] = int(input('hippity hoppity where do i go-ity '))
        self.orientation = self.data[arg1]
        self.v += 2
    #GET THE COMEDY NOTES BACK

    def opFour(self, arg1): #always just gives 0 1 or 2
        if arg1 == 0: #this wall can commit not alive
            pass
            #print('dumb droid haha')
        elif arg1 == 1: #well we moved
            self.move()
            if self.currPos not in self.coordinates:
                self.coordinates.append(self.currPos[:])
            #print(self.currPos)
            self.showMaze()
            self.doneMoving = True
            self.moveCheck = 0
        elif arg1 == 2: #HALLELUJAH
            self.move()
            if self.currPos not in self.coordinates:
                self.coordinates.append(self.currPos[:])
            self.foundOx == True
        #print(self.coordinates[-1])
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
        for x in range(min(xVals), max(xVals) + 1)  # just consists of all the points
        ]
        for p in code.coordinates:
            for pt in canvas:
                if pt[:2] == p[:2]:
                    canvas[canvas.index(pt)] = p + [True]
        goodCanvas = list(chunks(canvas, max(xVals) - min(xVals) + 1))
        #print(goodCanvas)
        goodCanvas.reverse()
        for chungus in goodCanvas:
            temp = ''
            for c in chungus:
                if c[-1]:
                    temp += ' O '
                else:
                    temp += '   '
            print(temp)

with open('data stuff/amazonElves.txt') as stuff:
    Data = [int(x) for x in stuff.readline().rstrip().split(sep = ',')]

#PART 1
code = Droid(Data)
code.interpret()
exit()
#THE BOTTOM PART JUST MAKES OUT A PATH: I JUST SOLVE IT BY HAND