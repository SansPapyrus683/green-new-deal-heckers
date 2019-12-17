from math import ceil
from sys import exit

data = open("data stuff/test.txt")
conversion = []  # each element: [product, reactants]
with data as Data:
    for line in data.readlines():
        temp = []
        line = line.rstrip().split(sep=" => ")
        line.reverse()
        temp.append([int(line[0].split()[0]), line[0].split()[1]])
        line = line[1].split(sep=", ")
        for r in line:
            r = r.split()
            temp.append([int(r[0]), r[1]])
        conversion.append(temp)
    elements = [k[1] for d in conversion for k in d]
    elements = list(set(elements))
    leftovers = {s: 0 for s in elements}
    print(conversion)


def findRawReactants(reactionList = conversion, element="FUEL", amt=1):
    """break everything down into ore components
    amt is the amt that we want produced
    oh and primitive elements are ones that can be directly
    made from just ore"""
    oreCount = 0
    for v, reaction in enumerate(reactionList):
        if reaction[0][-1] == element:
            increment = reaction[0][0]
            alreadyHave = leftovers[element]
            if amt >= alreadyHave:
                amt -= alreadyHave
                leftovers[element] = 0
            elif amt < alreadyHave:
                leftovers[element] = alreadyHave - amt
                alreadyHave -= amt
                continue
            productionTimes = ceil(amt / increment)
            #print(productionTimes, "times to do it")
            amtProduced = 0
            for i in range(productionTimes):  # does it enough to produce the amt
                for e in reaction[1:]:
                    if e[-1] == "ORE":
                        for i in range(productionTimes):
                            oreCount += e[0]
                            amtProduced += increment
                        leftovers[element] += amtProduced - amt
                        return increment, oreCount
                    else:
                        # print('finding the ore needed to produce %s of %s' %(e[0], e[1]))
                        for r in reactionList:
                            if r[0][1] == e[1]:
                                oreCount += findRawReactants(
                                    conversion, e[1], amt=e[0]
                                )[1]
                                break
                amtProduced += increment
            leftovers[element] += amtProduced - amt

    return increment, oreCount

#PART 1
print(findRawReactants(conversion, element="FUEL", amt=1)[1])

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