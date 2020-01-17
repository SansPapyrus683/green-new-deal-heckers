from iHateIntcode.justStupidIntcode import intCode, chunks
from sys import exit
# ok so i don't frickin care if you wanna see the beam

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


with open("finallySomeGoodFood.txt") as stuff:
    Data = [int(x) for x in stuff.readline().split(sep=",")]
    code = Beam(Data)

# PART 1
partOneRun = True
attracted = 0
if partOneRun:
    coordinates = [[x, y, 0] for y in range(50) for x in range(50)]
    for coo in coordinates:
        code.interpret()
    print("we be attracting %s things? idk" % attracted)

# PART 2
<<<<<<< HEAD
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

currYValCheck = 5
xCheckRange = range(6 - 2, 6 + 2 + 1)  # also there's this gap between the first and the rest
=======
currYValCheck = 5  # ill go row by row
xCheckRange = [6 - 2, 6 + 2 + 1]  # also there's this gap between the first and the rest
>>>>>>> 2f0072f4d32f3389fcdc797079824dc3b49ef6ef
shipDimension = 100
attractedRecords = [None] * shipDimension

while True:  # TODO: maybe optimize this somehow? maybe get the startrange better
    started = False
    record = []  # start and end (inclusive)
    start = xCheckRange[0]
    end = xCheckRange[1]  # these are just placeholders
    while True:
        coo = [start, currYValCheck, 0]
        code.interpret()
        if coo[-1]:
            record.append(start)
            break
        start += 1

    while True:
        coo = [end, currYValCheck, 0]
        code.interpret()
        if coo[-1]:
            record.append(end)
            break
        end -= 1

    xCheckRange = [(record[0] - 2), (record[1] + 2 + 1)]
    startRange = list(range(record[0], record[1] + 1))
    snapshotIndex = 0
    for i in range(len(startRange) + 1 - shipDimension):
        snapshot = startRange[snapshotIndex: snapshotIndex + shipDimension]
        ptsToBeChecked = [[snapshot[0], currYValCheck, False],   # generates corners of the square
                          [snapshot[-1], currYValCheck, False],
                          [snapshot[0], currYValCheck + shipDimension - 1, False],
                          [snapshot[-1], currYValCheck + shipDimension - 1, False]]
        for pt in ptsToBeChecked:
            coo = pt[:]
            code.interpret()
            if not coo[-1]:
                break
        else:
<<<<<<< HEAD
            print('aosidfpoasijdf', ptsToBeChecked)
=======
            print('santa you capitalist pig: %s' % ptsToBeChecked[0][:-1])
>>>>>>> 2f0072f4d32f3389fcdc797079824dc3b49ef6ef
            exit()
        snapshotIndex += 1
    currYValCheck += 1
