from math import ceil

data = open("data stuff/jason.txt")
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


def findRawReactants(reactionList, element="FUEL", amt=1):
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
                            if r[0][1] == e[1] and r[-1][1] == "ORE":
                                # print('%s is a primitive element' % e)
                                oreCount += findRawReactants(
                                    conversion, e[1], amt=e[0]
                                )[1]
                            elif r[0][1] == e[1]:
                                oreCount += findRawReactants(
                                    conversion, e[1], amt=e[0]
                                )[1]
                amtProduced += increment
            leftovers[element] += amtProduced - amt

    return increment, oreCount

#PART 1
print(findRawReactants(conversion, element="FUEL", amt=1)[1])

#PART 2
totalOre = 10 ** 12