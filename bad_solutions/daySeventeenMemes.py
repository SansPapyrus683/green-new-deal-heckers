# dont ask what happened to day sixteen
# we all miss it
from justStupidIntcode import intCode, ascii


class Scaffold(intCode):
    def __init__(self, code):
        super().__init__(code)
        self.xVal = 0
        self.yVal = 0
        self.coordinates = []

    def opFour(self, arg1):
        if arg1 == 35:
            print(" # ", end="")
            self.coordinates.append([self.xVal, self.yVal])
            self.xVal += 1
        elif arg1 == 46:
            print(" . ", end="")
            self.xVal += 1
        elif arg1 == 10:
            self.yVal += 1
            self.xVal = 0
            print("")
        self.v += 2


with open("data stuff/memlord.txt") as stuff:
    code = Scaffold([int(x) for x in stuff.readline().rstrip().split(sep=",")])
    code.interpret()
    # print(code.coordinates)

# PART 1
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
