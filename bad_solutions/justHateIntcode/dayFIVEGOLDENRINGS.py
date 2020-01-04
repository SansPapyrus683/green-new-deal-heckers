rings = open(
    "C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/goldenRings.txt"
)
# rings = open("test.txt")
with rings as data:
    for v, s in enumerate(data):
        Data = [int(x) for x in s.split(sep=",")]
# PART 1 and 2 lol- for part 1, put in a 1 but for part 2 put in a 5
from justStupidIntcode import intCode

intcode = intCode(Data)
intcode.interpret()
