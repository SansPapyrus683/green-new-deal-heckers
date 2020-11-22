from y2019.iHateIntcode.forStupidIntcode import IntCode

with open("goldenRings.txt") as data:
    for v, s in enumerate(data):
        Data = [int(x) for x in s.split(sep=",")]

# PART 1 and 2 lol- for part 1, put in a 1 but for part 2 put in a 5
intcode = IntCode(Data)
intcode.interpret()
