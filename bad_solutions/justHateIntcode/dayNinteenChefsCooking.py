from justStupidIntcode import intCode, chunks


class Beam(intCode):
    def __init__(self, code):
        super().__init__(code)
        self.count = 0

    def opThree(self, arg1):
        self.count += 1
        self.v += 2
        if self.count == 1:
            self.data[arg1] = coo[0]  # it'll be a variable implemented later
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


seeReading = True
if seeReading:
    coordinates = [[x, y, 0] for y in range(100) for x in range(100)]
    for coo in coordinates:
        code.interpret()
    showBeam()


def testPtSquare(pt=(0, 0), dimension=3):
    """generates a 100*100 square
    from a single point that is the upper left corner
    also, tests if it is valid"""
    borderTest = [[pt[0], pt[1], 0]]
    for i in range(dimension):
        borderTest.extend(([pt[0], pt[1] + i, 0], [pt[0] + i, pt[1], 0],
                           [pt[0] + i, pt[1] + 3, 0], [pt[0] + 3, pt[1] + i, 0]))
    borderTest = [list(pt) for pt in set([tuple(pt) for pt in borderTest])]
    print(borderTest)

    for coo in borderTest:
        code.interpret()
        if not coo[-1]:
            break
    else:
        return True
    return False


print(testPtSquare())
