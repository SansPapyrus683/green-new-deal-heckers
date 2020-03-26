"""dont question the name"""
import sys
sys.path.insert(1, 'C:\\Users\\kevin\\OneDrive\\Documents\\GitHub\\green-new-deal-heckers\\2019\\iHateIntcode')
from justStupidIntcode import intCode

with open("gardenTool.txt") as data:
    Data = [int(x) for x in data.readline().rstrip().split(sep=",")]
    code = intCode(Data)
    code.interpret()  # for part 1 put 1, for part 2 put 2
