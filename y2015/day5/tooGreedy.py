vowels = {'a', 'e', 'i', 'o', 'u'}

def goodBad(child):
    if 'ab' in child or 'cd' in child or 'pq' in child or 'xy' in child:
        return False

    vowelCount = 0
    doubleReq = False
    for v, c in enumerate(child):
        if child[v - 1] == c and v != 0:
            doubleReq = True
        if c in vowels:
            vowelCount += 1
    return doubleReq and vowelCount >= 3


def goodGoodBad(child):
    sandwichReq = False
    doubleDoubleReq = False
    doubleArchives = {}
    for v, c in enumerate(child):
        if v >= 2 and child[v - 2] == c:
            sandwichReq = True

        if v >= 1 and child[v - 1: v + 1] in child[v + 1:]:
            doubleDoubleReq = True
        doubleArchives[child[v - 1: v + 1]] = [v - 1, v]

    return sandwichReq and doubleDoubleReq

faultyGoods = 0
trulyGoods = 0
with open('blueOneTho') as read:
    for kid in read.readlines():
        if goodBad(kid.rstrip()):
            faultyGoods += 1

        if goodGoodBad(kid.rstrip()):
            trulyGoods += 1

print(faultyGoods, 'darn- only 1/5 of the kids are nice? what the heck! (part 1)')
print(trulyGoods, '?  THAT\'S EVEN LESS!! (part 2)')
