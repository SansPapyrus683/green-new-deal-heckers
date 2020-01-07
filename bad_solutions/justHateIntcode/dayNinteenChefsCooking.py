from justStupidIntcode import intCode, chunks


class Beam(intCode):
    def __init__(self, code):
        super().__init__(code)
        self.count = 0

    def opThree(self, arg1):
        """this uses a global variable coo (declared later)
        to put in the inputs because otherwise i have
        no idea at all how to implement it"""
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
    code = Beam(Data)

# PART 1
attracted = 0
partOneRun = False
if partOneRun:
    coordinates = [[x, y, 0] for y in range(50) for x in range(50)]
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


seeReading = False
if seeReading:
    coordinates = [[x, y, 0] for y in range(100) for x in range(100)]
    for coo in coordinates:
        code.interpret()
    showBeam()


def testPtSquare(pt=(0, 0), dimension=100):
    """generates a square whose dimension defaults to 100
    from a single point that is the upper left corner
    also, tests if it is valid"""
    borderTest = [[pt[0], pt[1], 0]]
    for i in range(dimension):
        borderTest.extend(([pt[0], pt[1] + i, 0], [pt[0] + i, pt[1], 0],
                           [pt[0] + i, pt[1] + dimension, 0], [pt[0] + dimension, pt[1] + i, 0]))
    borderTest = [list(pt) for pt in set([tuple(pt) for pt in borderTest])]
    # print(borderTest)

    for coo in borderTest:
        code.interpret()
        if not coo[-1]:
            break
    else:
        return True
    return False


currYValCheck = 5  # ill go row by row
xCheckRange = range(6-2, 6+2+1)  # also there's this gap between the first and the rest
shipDimension = 100

for i in range(10):
    started = False
    record = []  # start and end (inclusive)
    for checked in xCheckRange:
        coo = [checked, currYValCheck, 0]
        code.interpret()
        if coo[-1] and not started:
            record.append(checked)
            started = True
        if (not coo[-1]) and started:
            record.insert(0, checked - 1)
            break
    else:
        record.insert(0, checked)
    print(record)
    xCheckRange = range(record[0] - 2, record[1] + 2 + 1)
    print(xCheckRange)
    currYValCheck += 1
