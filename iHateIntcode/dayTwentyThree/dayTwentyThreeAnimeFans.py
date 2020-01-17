from iHateIntcode.justStupidIntcode import *
from queue import Queue
from sys import exit

class CategorySix(intCode):
    def __init__(self, codeIn, address):
        super().__init__(codeIn)
        self.inputQueue = Queue()
        self.networkAddress = address
        self.firstRun = True
        self.outputs = []
        self.outputCount = 0
        self.inputCount = 0
        self.inputtedPacket = False

    def opThree(self, arg1):
        if self.firstRun:
            self.data[arg1] = self.networkAddress
            self.firstRun = False
        else:
            if self.inputQueue.empty():
                self.data[arg1] = -1
                self.inputCount = 2
            else:
                self.receivePacket = self.inputQueue.get()
                self.data[arg1] = self.receivePacket[self.inputCount]
                self.inputCount += 1
                if self.inputCount == 2:
                    pass
            if self.inputCount == 2:
                pass
        self.v += 2

    def opFour(self, arg1):
        self.outputCount += 1
    def __str__(self):
        return f'computer at address %i' % self.networkAddress

with open('test.txt') as code:
    data = [int(i) for i in code.read().rstrip().split(sep=',')]

totalOutputs = []
for comp in computerList:
    print(comp)

while True:
    for output in totalOutputs:
        if output[0] == 255:
            print(output)
            exit()

    for nic in computerList:
        nic.interpret()
