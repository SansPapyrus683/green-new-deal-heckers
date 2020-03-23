"""IM NOT SANTA
IM JUST ROBBING A BANK IN NOVEMBER
but really im running out of ideas"""
file = open("bankInNovember")
sigCode = []
with file as data:
    for l in data.readlines():
        for s in l.rstrip():
            sigCode.append(int(s))

# PART 1
pattern = [0, 1, 0, -1]


def oneStep(code, times):
    for y in range(times):
        result = []
        for j in range(len(code)):
            nextPatterns = []
            for i in pattern:
                nextPatterns.extend([i for x in range(j + 1)])
            actualMatch = nextPatterns[1:]
            while len(actualMatch) < len(code):
                actualMatch.extend(nextPatterns)
            # print(actualMatch)
            tempSum = 0
            for v, x in enumerate(code):
                tempSum += x * actualMatch[v]
            result.append(int(str(tempSum)[-1]))
        code = result[:]
        # print(code)
    return code


partOneRun = True
if partOneRun:
    print('i don\'t think this sigcode:\n %i \n is even based in science' % oneStep(sigCode, 100))

# PART 2
offset = int("".join([str(s) for s in sigCode[:7]]))
whatWeWant = (sigCode * 10000)[offset:]
for i in range(100):
    masterSum = 0
    for x in range(len(whatWeWant) - 1, -1, -1):
        masterSum += whatWeWant[x]
        whatWeWant[x] = masterSum % 10
    # print('one time')

print('i hate you santa - %s' % whatWeWant[:8])
