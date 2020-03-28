numbers = ''
with open('reallyHurry.txt') as read:
    rightInHere = read.read().rstrip()
    for c in rightInHere:
        if c.isdigit() or c in [',', '-']:  # we just have to count the numbers, no recursion needed
            numbers += c  # (at first i implemented a recursive solution tho lol)
    hugeArray = eval(rightInHere)  # for part 2 only

numSum = 0
for n in numbers.split(sep=','):
    if n:  # the split gives me a lot of empty strings: this filters them out
        numSum += int(n)

print('santa\'s elves are the stupidest creatures ever: %i' % numSum)

# PART 2
def sumWORed(sumObj):
    totalSum = 0
    if isinstance(sumObj, list):  # for lists it doesn't matter
        goThrough = sumObj
    elif isinstance(sumObj, dict):
        if "red" in sumObj.values():  # don't even START counting if there's a red detected
            return 0
        goThrough = sumObj.values()
    elif isinstance(sumObj, int):
        return sumObj
    else:
        return 0

    for a in goThrough:
        if isinstance(sumObj, dict):
            totalSum += sumWORed(a)  # simple recursion
        elif isinstance(sumObj, list):
            totalSum += sumWORed(a)
        elif isinstance(sumObj, int):
            totalSum += a
    return totalSum

print('yup, santa\'s elves are insane in the membrane: %i' % sumWORed(hugeArray))
