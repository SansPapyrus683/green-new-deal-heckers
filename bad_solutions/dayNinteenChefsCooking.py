from justStupidIntcode import intCode, chunks


class Beam(intCode):
    def __init__(self, code):
        super().__init__(code)
        self.count = 0

    def opThree(self, arg1):
        self.count += 1
        self.v += 2
        if self.count == 1:
            self.data[arg1] = coo[0]
        elif self.count == 2:
            self.data[arg1] = coo[1]
            self.count = 0

    def opFour(self, arg1):
        global attracted
        if arg1 == 1:
            attracted += 1
            coo[-1] = 1
        self.v += 2


with open(
        "C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/finallySomeGoodFood"
) as stuff:
    Data = [int(x) for x in stuff.readline().split(sep=",")]

# PART 1
code = Beam(Data)
coordinates = [[x, y, 0] for y in range(50) for x in range(50)]
attracted = 0
for coo in coordinates:
    code.interpret()
print("we be attracting %s things? idk" % attracted)


# PART 2
# print(coordinates)
def showBeam():
    xVals = list(set([x[0] for x in coordinates]))
    for l in chunks(coordinates, max(xVals) - min(xVals) + 1):
        line = ""
        for c in l:
            if c[-1]:
                line += " # "
            else:
                line += " . "
        print(line)


coordinates = [[x, y, 0] for y in range(5, 100) for x in range(6, 100)]
for coo in coordinates:
    code.interpret()

seeReading = True
if seeReading:
    showBeam()


def genSquare(pt=[0, 0]):
    """generates a 100*100 square
    rom a single point that is the upper left corner"""

    for pt in [[x, y] for y in range(pt[1] + 100) for x in range(pt[0] + 100)]:
        yield pt


relativePosition = [6, 5]  # all coordinates from now will be relative to this point
