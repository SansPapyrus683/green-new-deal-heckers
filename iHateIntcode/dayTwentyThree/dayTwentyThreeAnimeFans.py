from iHateIntcode.justStupidIntcode import *
from queue import Queue


class CategorySix(intCode):
    def __init__(self, codeIn, address):
        super().__init__(codeIn)
        self.inputQueue = Queue()
        self.networkAddress = address
        self.outputs = []
        self.outputCount = 0
        self.inputCount = 0
        self.makeException = False  # this tells the program just stop right now even if there's no output
        self.indexToReturnTo = 0
        self.inputtingPacket = False
        self.firstTime = True

    def interpret(self):
        self.v = self.indexToReturnTo
        while self.v <= len(self.data):
            self.i = self.data[self.v]
            if self.i == 99 or self.makeException:  # breaks if finished inputting
                self.inputCount = 0
                self.indexToReturnTo = self.v
                self.makeException = False
                break
            self.translator(self.i)
            if self.i % 10 == 4:  # a separate case for when it spits out a buncha outputs
                if self.outputCount == 3:  # the computer has finished its outputting
                    self.indexToReturnTo = self.v
                    self.inputCount = 0
                    self.makeException = False
                    self.outputCount = 0
                    if goodPacketFound:
                        break
                    break

    def opThree(self, arg1):
        if self.inputCount == 2:  # it has hit another input and must be stopped
            self.makeException = True
            return  # frick off, you have to wait

        if self.firstTime:  # this makes a special exception for the computer running the first time
            self.data[arg1] = self.networkAddress
            print('first inputted this thing', self.networkAddress)
            self.inputCount = 2  # we've finished inputting for this cycle
            self.firstTime = False
            self.v += 2
            return

        if self.inputQueue.empty() and not self.inputtingPacket:
            print('ok we have nothing rn for computer %i' % self.networkAddress)
            self.data[arg1] = -1
            self.makeException = True
            self.inputCount = 2
        else:
            if self.inputCount == 0:
                self.receivePacket = self.inputQueue.get()  # only get one when we restart
                print('for computer %i, we have %s' % (self.networkAddress, self.receivePacket))
            self.data[arg1] = self.receivePacket[self.inputCount]
            print('inputted %i for computer %i' % (self.data[arg1], self.networkAddress))
            self.inputCount += 1
            self.inputtingPacket = True
        self.v += 2

    def opFour(self, arg1):
        global goodPacketFound
        self.outputCount += 1
        self.outputs.append(arg1)
        if self.outputCount == 3:
            totalOutputs.append(self.outputs)
            print('ok so this computer spit out %s into the pool of %s' % (self.outputs, totalOutputs))
            if self.outputs[0] == 255:
                print('HALLELUJAH', self.outputs)
                goodPacketFound = True
                self.v += 2
                return
            computerList[self.outputs[0]].inputQueue.put(self.outputs[1:])
            self.outputs = []
        self.v += 2


with open('test.txt') as code:
    data = [int(i) for i in code.read().rstrip().split(sep=',')]
    computerList = [CategorySix(data, i) for i in range(2)]

totalOutputs = []
goodPacketFound = False
while not goodPacketFound:
    for nic in computerList:
        print('continuing for computer %i' % nic.networkAddress)
        nic.interpret()
