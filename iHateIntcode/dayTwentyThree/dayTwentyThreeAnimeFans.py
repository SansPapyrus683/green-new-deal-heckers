from iHateIntcode.justStupidIntcode import *
from queue import Queue


class CategorySix(intCode):
    def __init__(self, codeIn, address):
        super().__init__(codeIn)
        self.inputQueue = Queue()
        self.networkAddress = address

    def opThree(self, arg1):
        self.v += 2

    def opFour(self, arg1):
        self.v += 2

    def __str__(self):
        print('computer at address %i' % self.networkAddress)

with open('animeIsTrash.txt') as code:
    data = [int(i) for i in code.read().rstrip().split(sep=',')]
    computerList = [CategorySix(data, x) for x in range(50)]

for comp in computerList:
    print(comp)