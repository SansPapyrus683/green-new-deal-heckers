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
        self.gotPacket = False

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
                self.gotPacket = True
        self.v += 2

    def opFour(self, arg1):
        self.outputCount += 1
        self.outputs.append(arg1)
        if self.outputCount == 3:
            totalOutputs.append(self.outputs)
            computerList[self.outputs[0]].inputQueue.put(self.outputs[1:])
            self.outputs = []
        self.v += 2

    def __str__(self):
        return f'computer at address %i' % self.networkAddress


with open('test.txt') as code:
    data = [int(i) for i in code.read().rstrip().split(sep=',')]
    computerList = [CategorySix(data, i) for i in range(2)]

totalOutputs = []
for comp in computerList:
    print(comp)

while True:
    if 255 in [out[0] for out in totalOutputs]:
        print(totalOutputs[[out[0] for out in totalOutputs].index(255)])
        break

    for nic in computerList:
        nic.interpret()
