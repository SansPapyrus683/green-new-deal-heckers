file = open("data stuff/test.txt")
sigCode = []
with file as data:
    for l in data.readlines():
        for s in l.rstrip():
            sigCode.append(int(s))

# PART 1
print(sigCode)
pattern = [0, 1, 0, -1]
