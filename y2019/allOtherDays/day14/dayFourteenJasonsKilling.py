from math import ceil
from sys import exit

data = open("jason.txt")
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
        for req in reactants.split(sep=", "):
            req = req.split()
            reac.append([int(req[0]), req[1]])
            elements.append(req[1])
        conversion[product[1]] = reac
    elements = list(set(elements))
    leftovers = {s: 0 for s in elements}


def findRawReactants(reactionList=conversion, element="FUEL", amt=1):
    """
    break everything down into ore components
    amt is the amt that we want produced
    oh and primitive elements are ones that can be directly
    made from just ore
    """
    oreCount = 0
    increment = reactionList[element][0]
    alreadyHave = leftovers[element]
    # print('well we already have %s of %s' % (alreadyHave, element))
    if amt >= alreadyHave:
        amt -= alreadyHave
        leftovers[element] = 0
    elif amt < alreadyHave:
        leftovers[element] -= amt
        # alreadyHave -= amt
        return 0
    productionTimes = ceil(amt / increment)  # calc the amt of times needed to produce
    amtProduced = 0
    # rint('for %s we need to make it %s times' % (element, productionTimes))
    for e in reactionList[element][1:]:
        if e[-1] == "ORE":
            oreCount += productionTimes * e[0]
        else:
            # print('finding the ore needed to produce %s of %s' %(e[0], e[1]))
            oreCount += findRawReactants(element=e[1], amt=productionTimes * e[0])
    amtProduced += increment * productionTimes
    leftovers[element] += amtProduced - amt

    return oreCount


# PART 1
print('wow- ONE UNIT OF FUEL costs this %i ore' % findRawReactants(conversion, element="FUEL", amt=1))

# PART 2
ORE_NUM = 10 ** 12

lowerBound = 0
upperBound = ORE_NUM
validSoFar = -1
while lowerBound <= upperBound:
    toSearch = (lowerBound + upperBound) // 2
    leftovers = {e: 0 for e in elements}
    if findRawReactants(amt=toSearch) < ORE_NUM:
        validSoFar = toSearch
        lowerBound = toSearch + 1
    else:
        upperBound = toSearch - 1

print("well we can make %s fuel - idk if thats enough" % validSoFar)
