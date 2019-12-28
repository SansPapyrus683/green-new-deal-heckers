from itertools import permutations
from justStupidIntcode import intCode

with open("C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/swanLake.txt") as data:
    for line in data.readlines():
        Data = [int(x) for x in line.rstrip().split(sep=",")]

# PART 2
class Amplifier(intCode):
    """an entirely seperate class just for the amplifier
    i seriously need to see a therapist"""

    def __init__(self, code, setting):
        self.data = code
        self.setting = setting
        self.returnIndex = 0
        self.stopped = False
        self.count = 0

    def interpret(self):
        self.v = self.returnIndex
        while self.v <= len(self.data):
            # print(self.v, self.data[self.v], self.count)
            self.i = self.data[self.v]
            if str(self.i)[-2:] == "99":  # way too simple so i just included it in here
                self.stopped = True
                break
            if self.i in [3, 4, 104]:
                if self.i == 3:
                    self.opThreeAmps(self.data[self.v + 1])
                    if self.count == 3:
                        break
                    continue
                elif self.i % 10 == 4:
                    self.opFourAmps(self.data[self.data[self.v + 1]])
                    continue
            self.translator(self.i)
        self.count = 0
        # we dont change it back

    def opThreeAmps(self, arg1):
        self.count += 1
        if self.count == 1:
            self.data[arg1] = self.setting
            self.v += 2
        elif self.count == 2:
            self.data[arg1] = self.output
            self.v += 2
            # kinda misleading, but its the output is the medium of exchange between two vars
        elif self.count == 3:
            self.returnIndex = self.v
            # this shows that the amplifier needs another input, so i stop it

    def opFourAmps(self, arg1):
        if str(self.i)[0] == 1:
            arg1 = self.data[self.v + 1]
        self.output = arg1
        self.v += 2


# PART 1
print(Data)
possibilites = permutations([0, 1, 2, 3, 4])
outputs = []
for a, b, c, d, e in possibilites:
    ampList = [
        Amplifier(Data[:], a),
        Amplifier(Data[:], b),
        Amplifier(Data[:], c),
        Amplifier(Data[:], d),
        Amplifier(Data[:], e),
    ]
    output = 0
    for amp in ampList:
        amp.output = output
        amp.interpret()
        output = amp.output
    outputs.append(output)
print("answer to pt 1:", max(outputs))

# PART 2
possibilites = permutations([5, 6, 7, 8, 9])
outputs = []
for a, b, c, d, e in possibilites:
    ampList = [
        Amplifier(Data[:], a),
        Amplifier(Data[:], b),
        Amplifier(Data[:], c),
        Amplifier(Data[:], d),
        Amplifier(Data[:], e),
    ]
    output = 0
    for amp in ampList:
        amp.output = output
        amp.interpret()
        output = amp.output
        # print(ampList[-1].stopped)
        # print('')
    if ampList[-1].stopped:
        # print(output)
        outputs.append(output)
    while True:
        for amp in ampList:
            # print('NOT FIRST TIME for timee for setting', amp.setting)
            amp.output = output
            amp.count = 1
            amp.interpret()
            output = amp.output
            # print('')
        if ampList[-1].stopped:
            outputs.append(output)
            break

print("part 2 ans:", max(outputs))
