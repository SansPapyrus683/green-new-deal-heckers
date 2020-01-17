from iHateIntcode.justStupidIntcode import intCode, chunks
from sys import exit


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
partOneRun = False
attracted = 0
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


seeReading = int(input('put 1 if you wanna see the beam and 0 if you don\'t '))
if seeReading:
    coordinates = [[x, y, 0] for y in range(100) for x in range(100)]
    for coo in coordinates:
        code.interpret()
    showBeam()

currYValCheck = 5  # ill go row by row
xCheckRange = range(6 - 2, 6 + 2 + 1)  # also there's this gap between the first and the rest
shipDimension = 2
attractedRecords = [None] * shipDimension

while True:  # TODO: maybe optimize this somehow?
    started = False
    record = []  # start and end (inclusive)
    for checked in xCheckRange:  # makes the line for the current y value
        coo = [checked, currYValCheck, 0]
        code.interpret()
        if coo[-1] and not started:
            record.append(checked)
            started = True
        if (not coo[-1]) and started:
            record.append(checked - 1)
            break
    else:
        record.append(checked)

    xCheckRange = range((record[0] - 2), (record[1] + 2 + 1))
    startRange = list(range(record[0], record[1] + 1))
    snapshotIndex = 0
    print(startRange)
    for i in range(len(startRange) + 1 - shipDimension):
        snapshot = startRange[snapshotIndex: snapshotIndex + shipDimension]
        print(snapshot, currYValCheck)
        ptsToBeChecked = [[snapshot[0], currYValCheck, False],   # generates corners of the square
                          [snapshot[-1], currYValCheck, False],
                          [snapshot[0], currYValCheck + shipDimension - 1, False],
                          [snapshot[-1], currYValCheck + shipDimension - 1, False]]
        print(ptsToBeChecked)
        for pt in ptsToBeChecked:
            coo = pt[:]
            code.interpret()
            if not coo[-1]:
                break
        else:
            print('aosidfpoasijdf', ptsToBeChecked)
        snapshotIndex += 1
    currYValCheck += 1
