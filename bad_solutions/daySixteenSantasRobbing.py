file = open("data stuff/bankInNovember")
sigCode = []
with file as data:
    for l in data.readlines():
        for s in l.rstrip():
            sigCode.append(int(s))

# PART 1
#print(sigCode)
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

print(oneStep(sigCode, 100))

#PART 2
sigCode = sigCode * 10000
print(oneStep(sigCode, 100))