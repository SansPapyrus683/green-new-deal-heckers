"""dont question the name"""
from y2019.iHateIntcode.intcodeUtils import IntCode

with open("gardenTool.txt") as data:
    Data = [int(x) for x in data.readline().rstrip().split(sep=",")]
    code = IntCode(Data)
    code.interpret()  # for part 1 put 1, for part 2 put 2
