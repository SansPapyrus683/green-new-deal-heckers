from justStupidIntcode import *
#norht south east west 1 2 3 4 -> x + 1, x - 1, y+ 1, y - 1
#wall 0 (position hasnt changed), 1 empty, 2 oxygen

class Droid(intCode):
    def __init__(self, code):
        super().__init__(code)
        self.coordinates = [[0,0,1]] #coordinates then thing
        self.currPos = [0, 0]
        self.foundOx = False

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
        self.data[arg1] = int(input('hippity hoppity where do i go-ity '))
        self.orientation = self.data[arg1]
        self.v += 2
    
    def opFour(self, arg1):
        if arg1 == 0:
            self.coordinates.append(self.currPos + [0])
        elif arg1 == 1:
            self.move()
            self.coordinates.append(self.currPos + [1])
        elif arg1 == 2:
            self.move()
            self.coordinates.append(self.currPos + [2])
            self.foundOx = True
        print(self.coordinates[-1])
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

    def testMove(self):
        self.copy = self.currPos[:]
        if self.orientation == 1:
            self.copy[1] += 1
        elif self.orientation == 2:
            self.copy[1] -= 1
        elif self.orientation == 3:
            self.copy[0] += 1
        elif self.orientation == 4:
            self.copy[0] -= 1
        return copy

with open('data stuff/amazonElves.txt') as stuff:
    Data = [int(x) for x in stuff.readline().rstrip().split(sep = ',')]

#PART 1
code = Droid(Data)
code.interpret()