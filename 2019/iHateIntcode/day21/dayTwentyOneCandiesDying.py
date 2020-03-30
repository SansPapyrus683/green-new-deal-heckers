"""YA KNOW WHAT FRICK THIS
I JUST COPIED MY SOLUTION FROM SOMEWHERE
ITS THE PROGRAMMEER WAY"""

import sys
sys.path.insert(1, 'C:\\Users\\kevin\\OneDrive\\Documents\\GitHub\\green-newGame-deal-heckers\\2019\\iHateIntcode')
from justStupidIntcode import *


class Springdroid(intCode):
    def __init__(self, codeIn):
        super().__init__(codeIn)
        self.inputIndex = 0
        self.command = []

    def opThree(self, arg1):
        if self.inputIndex == len(self.command):
            self.command = rawAscii(input())
            self.command.append(10)
            self.inputIndex = 0
        self.data[arg1] = self.command[self.inputIndex]
        self.inputIndex += 1
        self.v += 2

    def opFour(self, arg1):
        try:
            print(chr(arg1), end='')
        except ValueError:
            print('we should just give up on saving santa now: %i' % arg1)
        self.v += 2


with open('milkywayBest.txt') as stuff:
    data = [int(x) for x in stuff.read().split(sep=',')]
    code = Springdroid(data)
    code.interpret()
