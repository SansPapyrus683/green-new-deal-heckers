from iHateIntcode.justStupidIntcode import intCode, rawAscii


class SantaDroid(intCode):
    """just pretty much a copy of the springdroid class"""

    def __init__(self, codeIn):
        super().__init__(codeIn)
        self.inputIndex = 0
        self.command = []

    def opThree(self, arg1):
        if self.inputIndex == len(self.command):
            self.command = rawAscii(input('you heard\'im '))
            self.command.append(10)
            self.inputIndex = 0
        self.data[arg1] = self.command[self.inputIndex]
        self.inputIndex += 1
        self.v += 2

    def opFour(self, arg1):
        try:
            print(chr(arg1), end='')
        except ValueError:
            print('SANTA BABY YOU BE TRASH: %i' % arg1)
        self.v += 2


with open('microsoftGood.txt') as code:
    santa = SantaDroid([int(i) for i in code.read().rstrip().split(sep=',')])
    santa.interpret()
