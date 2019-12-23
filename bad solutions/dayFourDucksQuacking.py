data = [273025, 767253]
count = 0
# PART 1- TESTVALID ONLY APPLIES FOR THIS ONE
def testValid(value):
    i = [int(x) for x in list(str(value))]
    previousVal = -1
    for y in i:
        if not y >= previousVal:
            return False
        previousVal = y
    for x in range(5):
        if i[x] == i[x + 1]:
            return True


for i in range(data[0], data[1] + 1):  # actuall runs the program
    if testValid(i):
        count += 1
print(count)

# PART 2 TEST VALID
def testValid(value):
    i = [int(x) for x in list(str(value))]
    previousVal = -1
    for y in i:
        if not y >= previousVal:
            return False
        previousVal = y
    guaranteedTrue = False
    for x in range(5):
        if x == 0:
            if i[x] == i[x + 1]:
                # print('lol')
                if i[x + 1] == i[x + 2]:
                    continue
                else:
                    return True
        elif x == 4:
            if i[x] == i[x + 1]:
                if i[x] == i[x - 1]:
                    continue
                else:
                    return True
        elif i[x] == i[x + 1]:
            if i[x] == i[x - 1] or i[x + 1] == i[x + 2]:
                pass
            else:
                return True
    else:
        return False


newCount = 0
for i in range(data[0], data[1] + 1):
    if testValid(i):
        newCount += 1
print(newCount)
