from justStupidIntcode import *
from collections import defaultdict
#this one is cold and calculating
#for the fun one go to dayThirteenCodersPlaying

class Arcade(intCode):
    def __init__(self, code):
        self.data = code
        self.data = defaultdict(int)
        for v, i in enumerate(code):
            self.data[v] = i
        self.relBase = 0
        self.outputs = []
        self.score = 0
        self.calcScore = False

    def opThree(self, arg1):
        # self.data[arg1] = int(input("*atari intensifies* "))
        x = processOutputs()
        self.ballPos, self.boardPos = x[1][:2], x[2][:2]
        self.score = x[0]
        self.v += 2
        self.data[arg1] = sign(self.ballPos[0] - self.boardPos[0])
        #print(sign(self.ballPos[0] - self.boardPos[0]))

    def opFour(self, arg1):
        # print(arg1)
        self.outputs.append(arg1)
        self.v += 2


def processOutputs():
    procsessed = []
    result = []
    for chungus in chunks(code.outputs, 3):
        procsessed.append(chungus)
    procsessed.reverse()
    #print(procsessed)
    for l in procsessed:
        if l[:2] == [-1, 0]:
            result.append(l[-1])
            procsessed.remove(l)
            print("Score: %s" % l[-1])
            break
    for chungus in chunks(procsessed, max(a[0] for a in procsessed) + 1):
        #print(chungus)
        for pt in chungus:
            if pt[-1]:
                if pt[-1] == 3: #paddle detected
                    result.append(pt)
                elif pt[-1] == 4: #ball detected
                    result.append(pt)
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
code.score = processOutputs()[0] #just process the outputs one more time
print('Total score: %s' % code.score)
