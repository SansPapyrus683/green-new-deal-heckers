from itertools import permutations
import sys
sys.path.insert(1, 'C:\\Users\\kevin\\OneDrive\\Documents\\GitHub\\green-newGame-deal-heckers\\2019\\iHateIntcode')
from justStupidIntcode import intCode

with open('mineTurtle.txt') as code:
    data = [int(x) for x in code.read().rstrip().split(sep=',')]
data[1], data[2] = 12, 2
values = [[a, b] for (a, b) in permutations(list(range(0, 100)), 2)]

# first part
intcode = intCode(data)
intcode.interpret()
print(intcode.changed[0])

# second part
with open('mineTurtle.txt') as code:
    data = [int(x) for x in code.read().rstrip().split(sep=',')]

for possibleValue in values:
    newIntCode = intCode(data)
    newIntCode.data[1], newIntCode.data[2] = possibleValue[0], possibleValue[1]
    newIntCode.interpret()
    if newIntCode.changed[0] == 19690720:
        print(possibleValue)
        break
