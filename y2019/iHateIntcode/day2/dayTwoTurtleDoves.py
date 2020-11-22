from itertools import permutations
from y2019.iHateIntcode.forStupidIntcode import IntCode

with open('mineTurtle.txt') as code:
    data = [int(x) for x in code.read().rstrip().split(sep=',')]
data[1], data[2] = 12, 2
values = [[a, b] for (a, b) in permutations(list(range(0, 100)), 2)]

# first part
intcode = IntCode(data)
intcode.interpret()
print("ok buddy- %s" % intcode.changed[0])

# second part
with open('mineTurtle.txt') as code:
    data = [int(x) for x in code.read().rstrip().split(sep=',')]

for possibleValue in values:
    newIntCode = IntCode(data)
    newIntCode.data[1], newIntCode.data[2] = possibleValue[0], possibleValue[1]
    newIntCode.interpret()
    if newIntCode.changed[0] == 19690720:
        print("just wondering if this is turing complete lol: %s", possibleValue)
        break
