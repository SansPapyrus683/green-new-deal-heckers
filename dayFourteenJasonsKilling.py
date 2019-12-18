from math import ceil
from sys import exit

data = open("data stuff/test.txt")
conversion = {}  # each element: [product, reactants]
with data as Data:
    elements = []
    for line in data.readlines():
        line = line.rstrip().split(sep=" => ")
        product = line[1]
        reactants = line[0]
        product = product.split()
        reac = [int(product[0])]
        elements.append(product[1])
        for req in reactants.split(sep = ', '):
            req = req.split()
            reac.append([int(req[0]), req[1]])
            elements.append(req[1])
        conversion[product[1]] = reac
    elements = list(set(elements))
    leftovers = {s: 0 for s in elements}
    print(conversion)
    print(elements)

def findRawReactants(reactionList = conversion, element="FUEL", amt=1):
    """break everything down into ore components
    amt is the amt that we want produced
    oh and primitive elements are ones that can be directly
    made from just ore"""
    oreCount = 0
    increment = reactionList[element][0]
    alreadyHave = leftovers[element]
    if amt >= alreadyHave:
        amt -= alreadyHave
        leftovers[element] = 0
    elif amt < alreadyHave:
        leftovers[element] = alreadyHave - amt
        alreadyHave -= amt
    productionTimes = ceil(amt/increment) #calc the amt of times needed to produce
    amtProduced = 0
    for i in range(productionTimes):  # does it enough to produce the amt
        for e in reactionList[element][1:]:
            if e[-1] == "ORE":
                oreCount += e[0]
                amtProduced += increment
            else:
                # print('finding the ore needed to produce %s of %s' %(e[0], e[1]))
                oreCount += findRawReactants(element = e[1], amt = e[0])
                amtProduced += increment
    leftovers[element] += amtProduced - amt

    return oreCount

#PART 1
print(findRawReactants(conversion, element="FUEL", amt=1))
print(leftovers)
exit()
#PART 2
oreNum = 10**12
#1 trillion is 12 0's
currNum = oreNum//2
searchRange = [1, oreNum]
while searchRange[1] - searchRange[0] > 1:
    leftovers = {s: 0 for s in elements}
    reference = findRawReactants(amt = currNum)[1]
    if reference < oreNum: #GIMME MORE
        searchRange[0] += (searchRange[1] - searchRange[0] + 1)//2
        currNum += (searchRange[1] - searchRange[0] + 1)//2
    elif reference > oreNum: #ooh thats a diddly darn too much
        searchRange[1] -= (searchRange[1] - searchRange[0] + 1)//2
        currNum -= (searchRange[1] - searchRange[0] + 1)//2
    else:
        print('ok we can make this much ore %s' % currNum)
        exit()
    print('searched one time')

print('well we have this, so... %s' % searchRange[0])