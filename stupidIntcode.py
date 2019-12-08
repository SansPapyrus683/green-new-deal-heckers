class intCode:
    """if you wanna kno what the frick this does,
    just go on advent of code 2019 im too lazy to explain it myself"""
    def __init__(self, code, amps = None):
        self.data = code
        self.ampSettings = amps
    def interpret(self):
        self.v = 0
        self.reference = self.data.copy()
        if self.ampSettings:
            self.count = 0
            self.output = 0
        while self.v <= len(self.data):
            self.i = self.tData[self.v]
            if self.i in [1,2,3,4,5,6,7,8,99]:
                if self.i == 99:
                    break
                opCode = self.i
                if opCode == 1: self.opOne(self.data[self.data[v+1]], self.data[self.data[v+2]], self.data[v+3])
                elif opCode == 2: self.opTwo(self.data[self.data[v+1]], self.data[self.data[v+2]], self.data[v+3])
                elif opCode == 3: self.opThree(self.data[v+1])
                elif opCode == 4: self.opFour(self.data[v+1])
                elif opCode == 5: self.opFive(self.data[self.data[v+1]], self.data[self.data[v+2]])
                elif opCode == 6: self.opSix(self.data[self.data[v+1]], self.data[self.data[v+2]])
                elif opCode == 7: self.opSeven(self.data[self.data[v+1]], self.data[self.data[v+2]], self.data[v+3])
                elif opCode == 8: self.opEight(self.data[self.data[v+1]], self.data[self.data[v+2]], self.data[v+3])
            if str(self.i)[-2:] in ['01', '02', '05', '06', '07', '08', '99']:
                if str(self.i)[-2:] == '99':
                    break
                self.stupidImmediate(self.i)
        self.data = self.reference.copy()
    def stupidImmediate(self, opCode):
        if str(opCode)[-1] in ['1', '2', '7', '8']:
            opCode = str(opCode).zfill(5)
            argList = []
            opCodeArgs = list(opCode[:3]); opCodeArgs.reverse()
            for v, x in enumerate(opCodeArgs):
                if x == '1': #immediate
                    argList.append(self.data[self.v + v + 1])
                elif x == '0': #positional
                    if v == 2:
                        argList.append(self.data[v+3+1]) #its always written to
                    else:
                        argList.append(self.data[self.data[self.v + v + 1]])
            read = int(str(opCode)[-1])
            if read == 1: self.opOne(argList[0], argList[1], argList[2])
            elif read == 2: self.opTwo(argList[0], argList[1], argList[2])
            elif read == 7: self.opSeven(argList[0], argList[1], argList[2])
            elif read == 8: self.opEight(argList[0], argList[1], argList[2])
        else: #stupid 5 and 6
            opCode = str(opCode).zfill(4)
            argList = [] #the arg to test, the immediate value to jump to
            opCode = list(opCode[:2]); opCode.reverse()
            for v, x in enumerate(opCode):
                if x == '1':
                    argList.append(self.data[self.data[self.v + v + 1]])
                if x == '0':
                    argList.append(self.data[self.data[self.v + 1]])
            read = int(str(opCode)[-1])
            if read == 5: self.opFive(argList[0], argList[1])
            elif read == 6: self.opSix(argList[0], argList[1])
    #arguments which the computer compares will be immediate- writes to is positional
    def opOne(self, arg1, arg2, arg3): 
        self.data[arg3] = arg1 + arg2
    def opTwo(self, arg1, arg2, arg3):
        self.data[arg3] = arg1 * arg2
    def opThree(self, arg1):
        self.data[arg1] = input('idk just put something ')
    def opFour(self, arg1):
        print(self.data[arg1])
    def opFive(self, arg1, arg2):
        if arg1:
            self.v = arg2
    def opSix(self, arg1, arg2, arg3): 
        if not arg1:
            self.v = arg2
    def opSeven(self, arg1, arg2, arg3):
        if arg1 < arg2:
            self.data[arg3] = 1
        else:
            self.data[arg3] =  0
    def opEight(self, arg1, arg2, arg3):
        if arg1 == arg2:
            self.data[arg3] = 1
        else:
            self.data[arg3] =  0