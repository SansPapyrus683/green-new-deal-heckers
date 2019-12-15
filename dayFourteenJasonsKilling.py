from math import ceil

data = open('data stuff/test.txt')
conversion = [] #each element: [product, reactants]
with data as Data:
    for line in data.readlines():
        temp = []
        line = line.rstrip().split(sep = ' => ')
        line.reverse()
        temp.append([int(line[0].split()[0]), line[0].split()[1]])
        line = line[1].split(sep = ', ')
        for r in line:
            r = r.split()
            temp.append([int(r[0]), r[1]])
        conversion.append(temp)

print(conversion)
elements = [k[1] for d in conversion for k in d]
elements = list(set(elements))
leftovers = {s: 0 for s in elements}
print(leftovers)

def findRawReactants(reactionList, element = 'FUEL', amt = 1):
    """break everything down into ore components
    amt is the amt that we want produced"""
    oreCount = 0
    for v, reaction in enumerate(reactionList):
        if reaction[0][-1] == element:
            increment = reaction[0][0]
            for e in reaction[1:]:
                if e[-1] == 'ORE':
                    productionTimes = ceil(amt/e[0])
                    amtProduced = 0
                    for i in range(productionTimes):
                        oreCount += e[0]
                        amtProduced += increment
                    leftovers[element] += amtProduced - amt
                else:
                    print(e)
                    for r in reactionList:
                        if r[0][1] == e[1] and r[-1][1] == 'ORE':
                            print('%s is a primitive element' % e)
                            oreCount += findRawReactants(conversion, e[1], amt = e[0])[1]
                    for el in reactionList:
                        
                        pass
    print(increment, oreCount)
    return increment, oreCount

findRawReactants(conversion, element = 'D', amt = 13)
print(leftovers)