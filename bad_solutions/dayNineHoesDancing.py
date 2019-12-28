"""dont question the name"""
from justStupidIntcode import intCode

with open(
    "C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/gardenTool.txt"
) as data:
    Data = [int(x) for x in data.readline().rstrip().split(sep=",")]
    code = intCode(Data)
    code.interpret()
