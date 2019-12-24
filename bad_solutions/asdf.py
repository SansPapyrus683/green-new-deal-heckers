#testing chamber
file = open("data stuff/test.txt")
sigCode = []
with file as data:
    for l in data.readlines():
        for s in l.rstrip():
            sigCode.append(int(s))

goodHalf = sigCode * 10000
pattern = [0, 1, 0, -1]
offset = int(''.join([str(s) for s in sigCode[:8]]))
print(offset)