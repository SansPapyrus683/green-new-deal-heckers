from justStupidIntcode import *
from sys import exit
#norht south east west 1 2 3 4 -> x + 1, x - 1, y+ 1, y - 1
#wall 0 (position hasnt changed), 1 empty, 2 oxygen
#right up left down or 3 1 2 4
class Droid(intCode):
    def __init__(self, code):
        super().__init__(code)
        self.coordinates = [[0,0,1]] #coordinates then thing
        self.currPos = [0, 0]
        self.foundOx = False
        self.orientation = 3 #start facing right bc why not
        self.moveBack = [0, False]

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
    #GET THE COMEDY NOTES BACK

    def opFour(self, arg1): #always just gives 0 1 or 2
        if arg1 == 0: #this wall can commit not alive
            print('dumb droid haha')
            if self.currPos not in self.coordinates:
                self.coordinates.append(self.currPos)
        elif arg1 == 1: #well we moved
            self.move()
            if self.currPos not in self.coordinates:
                self.coordinates.append(self.currPos)
            print(self.currPos)
        elif arg1 == 2: #HALLELUJAH
            self.move()
            self.coordinates.append(self.currPos + [2])
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

with open('data stuff/amazonElves.txt') as stuff:
    Data = [int(x) for x in stuff.readline().rstrip().split(sep = ',')]

#PART 1
code = Droid(Data)
code.interpret()
