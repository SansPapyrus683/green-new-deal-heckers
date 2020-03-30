import sys
sys.path.insert(1, 'C:\\Users\\kevin\\OneDrive\\Documents\\GitHub\\green-newGame-deal-heckers\\2019\\iHateIntcode')
from justStupidIntcode import intCode

with open("goldenRings.txt") as data:
    for v, s in enumerate(data):
        Data = [int(x) for x in s.split(sep=",")]

# PART 1 and 2 lol- for part 1, put in a 1 but for part 2 put in a 5
intcode = intCode(Data)
intcode.interpret()
