"""dont question the name"""
from iHateIntcode.justStupidIntcode import intCode

with open("gardenTool.txt") as data:
    Data = [int(x) for x in data.readline().rstrip().split(sep=",")]
    code = intCode(Data)
    code.interpret()
