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
                self.inputtingPacket = False
                break
            self.translator(self.i)

    def opThree(self, arg1):
        if self.inputCount == 2:  # it has hit another input and must be stopped
            self.makeException = True
            return  # frick off, you have to wait

        if self.firstTime:  # this makes a special exception for the computer running the first time
            self.data[arg1] = self.networkAddress
            self.inputCount = 2  # we've finished inputting for this cycle, see above for exception-making
            self.firstTime = False
            self.v += 2
            return

        if self.inputQueue.empty() and not self.inputtingPacket:
            print('nothing rn for %s' % self.networkAddress)
            self.data[arg1] = -1
            self.makeException = True
            self.inputCount = 2
        else:
            if self.inputCount == 0:
                self.receivedPacket = self.inputQueue.get()  # only get one when we restart
            self.data[arg1] = self.receivedPacket[self.inputCount]
            print('inputted %i for computer %i' % (self.data[arg1], self.networkAddress))
            self.inputCount += 1
            self.inputtingPacket = True
        self.v += 2

    def opFour(self, arg1):
        global natThing, idleCount
        self.outputCount += 1
        self.outputs.append(arg1)
        if self.outputCount == 3:
            totalOutputs.append(self.outputs)
            print('spat out %s' % self.outputs)
            idleCount = 0
            if self.outputs[0] == 255:
                print('ha- who\'s the god now, google? %s (oh by the way it\'s part 1 ans)' % self.outputs)
                natThing = self.outputs[1:]
                self.v += 2
                return
            computerList[self.outputs[0]].inputQueue.put(self.outputs[1:])
            self.outputs = []
            self.outputCount = 0
        self.v += 2


with open('animeIsTrash.txt') as code:
    computerNumber = 50
    data = [int(i) for i in code.read().rstrip().split(sep=',')]
    computerList = [CategorySix(data, i) for i in range(computerNumber)]

totalOutputs = []
natThing = []
natZeroCount = 0  # keeps track of how many times nat has sent stuff to 0 (in a row)
idleCount = 0
firstCycle = True
while True:
    if not firstCycle:
        for comp in computerList:
            if not comp.inputQueue.empty():
                idleCount = 0
                natZeroCount = 0
                break
        else:  # ok, so all the input queues are empty, so it half-considers it idle
            idleCount += 1
            if idleCount == 3:
                print('declared idle', natThing)
                computerList[0].inputQueue.put(natThing)
                natZeroCount += 1
                if natZeroCount == 2:
                    print(natThing, 'aaaa')
                    exit()
                idleCount = 0

    print('')
    for nic in computerList:
        nic.interpret()

    firstCycle = False