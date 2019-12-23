"""dont question the name"""
from justStupidIntcode import intCode

with open("data stuff/gardenTool.txt") as data:
    Data = [int(x) for x in data.readline().rstrip().split(sep=",")]
    code = intCode(Data)
    code.interpret()
