from collections import defaultdict

"""just a bunch of functions that i might use later on"""


class intCode:
    """if you wanna kno what the frick this does,
    just go on advent of code 2019 im too lazy to explain it myself
    im gonna have nightmares about 203
    but it just interprets intcode thats all ill tall you"""

    def __init__(self, code):
        self.data = code
        self.data = defaultdict(int)
        for v, i in enumerate(code):
            self.data[v] = i
        self.relBase = 0

    def interpret(self):
        self.v = 0
        self.reference = self.data.copy()
        self.currSetting = 0
        while self.v <= len(self.data):
            # print(self.v, self.data[self.v])
            self.i = self.data[self.v]
            if str(self.i)[-2:] == "99":  # way too simple so i just included it in here
                break
            self.translator(self.i)

        self.changed = self.data
        self.data = self.reference.copy()  # to change it back to the original

    def translator(self, opCode):
        """tanslates opcode with args into good stuff
        im just putting all opcodes with their arguments into this lol"""
        if str(opCode)[-1] in ["1", "2", "7", "8"]:  # these have 4 arguments
            opCode = str(opCode).zfill(5)
            argList = []
            opCodeArgs = list(opCode[:3])
            opCodeArgs.reverse()

            for v, x in enumerate(opCodeArgs):  # writes out the actual arglist
                if x == "1":  # immediate
                    argList.append(self.data[self.v + v + 1])
                elif x == "0":  # positional
                    if v == 2:
                        argList.append(self.data[self.v + 3])  # its always written to
                    else:
                        argList.append(self.data[self.data[self.v + v + 1]])
                elif x == "2":  # relative
                    if v == 2:
                        argList.append(self.data[self.v + 3] + self.relBase)
                    else:
                        argList.append(
                            self.data[self.data[self.v + v + 1] + self.relBase]
                        )

            read = int(str(opCode)[-1])
            if read == 1:
                self.opOne(argList[0], argList[1], argList[2])
            elif read == 2:
                self.opTwo(argList[0], argList[1], argList[2])
            elif read == 7:
                self.opSeven(argList[0], argList[1], argList[2])
            elif read == 8:
                self.opEight(argList[0], argList[1], argList[2])

        elif str(opCode)[-1] in [
            "5",
            "6",
        ]:  # stupid 5 and 6, which only have 2 arguments
            opCode = str(opCode).zfill(4)
            argList = []  # the arg to test, the immediate value to jump to
            opCodeArgs = list(opCode[:2])
            opCodeArgs.reverse()

            for v, x in enumerate(opCodeArgs):
                if x == "1":
                    argList.append(self.data[self.v + v + 1])
                if x == "0":
                    argList.append(self.data[self.data[self.v + v + 1]])
                if x == "2":
                    argList.append(self.data[self.data[self.v + v + 1] + self.relBase])

            read = int(str(opCode)[-1])
            if read == 5:
                self.opFive(argList[0], argList[1])
            elif read == 6:
                self.opSix(argList[0], argList[1])

        elif str(opCode)[-1] in ["4", "3", "9"]:  # opcode 4 and 9 only has 1 argument
            opCode = str(opCode).zfill(3)
            opCodeArg = int(str(opCode)[0])
            read = int(opCode[-1])

            if opCodeArg == 1:
                if read == 4:
                    self.opFour(self.data[self.v + 1])
                elif read == 9:
                    self.opNine(self.data[self.v + 1])
            elif opCodeArg == 0:
                if read == 4:
                    self.opFour(self.data[self.data[self.v + 1]])
                elif read == 9:
                    self.opNine(self.data[self.data[self.v + 1]])
                elif read == 3:
                    self.opThree(self.data[self.v + 1])
            elif opCodeArg == 2:
                if read == 4:
                    self.opFour(self.data[self.data[self.v + 1] + self.relBase])
                elif read == 3:
                    self.opThree(arg1=(self.data[self.v + 1] + self.relBase))
                elif read == 9:
                    self.opNine(self.data[self.data[self.v + 1] + self.relBase])

    def opOne(self, arg1, arg2, arg3):
        self.data[arg3] = arg1 + arg2
        self.v += 4

    def opTwo(self, arg1, arg2, arg3):
        self.data[arg3] = arg1 * arg2
        self.v += 4

    def opThree(self, arg1):
        # print('setting data at %s index' % arg1)
        self.data[arg1] = int(input("idk just put something "))
        self.v += 2

    def opFour(self, arg1):
        print(arg1)
        self.v += 2

    def opFive(self, arg1, arg2):
        if arg1 != 0:
            self.v = arg2
        else:
            self.v += 3

    def opSix(self, arg1, arg2):
        if arg1 == 0:
            self.v = arg2
        else:
            self.v += 3

    def opSeven(self, arg1, arg2, arg3):
        if arg1 < arg2:
            self.data[arg3] = 1
        else:
            self.data[arg3] = 0
        self.v += 4

    def opEight(self, arg1, arg2, arg3):
        if arg1 == arg2:
            self.data[arg3] = 1
        else:
            self.data[arg3] = 0
        self.v += 4

    def opNine(self, arg1):
        self.relBase += arg1
        self.v += 2


def chunks(lst, n):
    """Yield successive n-sized chunks from lst. shamless copied from
    stack overflow lol"""
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


def sign(n):
    """need i say more?"""
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


def ascii(before: str) -> list:
    return list(map(ord, before))


if __name__ == "__main__":
    with open("dayNine/gardenTool.txt") as data:
        Data = [int(x) for x in list(data.readline().rstrip().split(sep=","))]
        code = intCode(Data)
        code.interpret()

    print('chunks test')
    for chungus in chunks([1, 2, 3, 4, 5, 6], 3):
        print(chungus)

    print('sing function test')
    print(sign(8), sign(-9), sign(0))

    print('ascii test')
    print(ascii("8,9"))
    print(ascii('what the heck'))
