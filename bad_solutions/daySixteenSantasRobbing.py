"""IM NOT SANTA
IM JUST ROBBING A BANK IN NOVEMBER
but really im running out of ideas"""
file = open("data stuff/bankInNovember")
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
            #print(actualMatch)
            tempSum = 0
            for v, x in enumerate(code):
                tempSum += x* actualMatch[v]
            result.append(int(str(tempSum)[-1]))
        code = result[:]
        #print(code)   
    return code         

partOneRun = False
if partOneRun:
    print(oneStep(sigCode, 100))

#PART 2
offset = int(''.join([str(s) for s in sigCode[:7]]))
whatWeWant = (sigCode * 10000)[offset:]
print(offset)
for i in range(100):
    masterSum = sum(whatWeWant)
    result = []
    for v, n in enumerate(whatWeWant):
        result.append(masterSum % 10)
        masterSum -= n
    whatWeWant = result
    #print('one time')

print(whatWeWant[:8])