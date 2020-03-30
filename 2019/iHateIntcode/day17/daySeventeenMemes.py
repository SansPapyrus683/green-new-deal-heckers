import sys
sys.path.insert(1, 'C:\\Users\\kevin\\OneDrive\\Documents\\GitHub\\green-newGame-deal-heckers\\2019\\iHateIntcode')
from justStupidIntcode import intCode


class Scaffold(intCode):
    def __init__(self, code):
        super().__init__(code)
        self.xVal = 0
        self.yVal = 0
        self.coordinates = []
        self.funcCount = 0  # keep track of which function we're inputting
        self.direCount = 0  # keeps track of the very number

    def opThree(self, arg1):
        self.direCount += 1
        self.data[arg1] = allFuncs[self.funcCount][self.direCount - 1]
        # print("inputted %s" % allFuncs[self.funcCount][self.direCount - 1])

        if allFuncs[self.funcCount][self.direCount - 1] == 10:
            self.funcCount += 1
            self.direCount = 0
        self.v += 2

    def opFour(self, arg1):
        try:
            print(" " + chr(arg1) + " ", end="")
        except ValueError:
            print("SPAAAACEDUUUUUST: %i" % arg1)

        """when its my funeral people will open the casket only to reveal
        that im not inside- instead, the space jam theme will play and they
        will see my corpse spinning around on a ceiling fan"""

        if arg1 in [35, 94, 62, 60, 118]:
            self.coordinates.append([self.xVal, self.yVal])
            self.xVal += 1
        elif arg1 == 46:
            self.xVal += 1
        elif arg1 == 10:
            self.yVal += 1
            self.xVal = 0
        self.v += 2


with open("memlord.txt") as stuff:
    code = Scaffold([int(x) for x in stuff.readline().rstrip().split(sep=",")])

# PART 1
code.interpret()
alignParaSum = 0
for c in code.coordinates:
    testee = [[c[0] + 1, c[1]], [c[0] - 1, c[1]], [c[0], c[1] + 1], [c[0], c[1] - 1]]
    for t in testee:
        if not t in code.coordinates:
            break
    else:
        # print(c[0], c[1], c[0] * c[1])
        alignParaSum += c[0] * c[1]
print("The sum of the alignment parameters is %s" % alignParaSum)

# PART 2
code.data[0] = 2
mainFunc = [65, 44, 66, 44, 65, 44, 66, 44, 67, 44, 67, 44, 66, 44, 65, 44, 66, 44, 67, 10, ]
funcA = [76, 44, 49, 48, 44, 82, 44, 49, 48, 44, 76, 44, 49, 48, 44, 76, 44, 49, 48, 10]
funcB = [82, 44, 49, 48, 44, 82, 44, 49, 50, 44, 76, 44, 49, 50, 10]
funcC = [82, 44, 49, 50, 44, 76, 44, 49, 50, 44, 82, 44, 54, 10]
allFuncs = [mainFunc, funcA, funcB, funcC, [110, 10]]  # <- last one is NO
code.interpret()
# see data stuff/heckingScaffolding for my movement pattern
