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
def findRawReactants(reactionList, element = 'FUEL', amtNeeded = 1):
    """break everything down into ore components"""
    oreCount = 0
    for v, reaction in enumerate(reactionList):
        if reaction[0][1] == element:
            increment = reaction[0][0]
            #print(increment)
            if reaction[1][1] == 'ORE': #its only ore when its used
                oreCount += reaction[1][0]
                #print('current orecount',oreCount)
                return increment, oreCount, oreCount - amtNeeded
            else:
                print(reaction)
                for el in reaction[1:]:
                    x = findRawReactants(reactionList[:v] + reactionList[v + 1:], el[1], el[0])
                    oreCount += x[1]
                    print(x)
                    print('Orecount for element %s: %s but it left over %s' %(el, x[1], x[2]))
    return increment, oreCount, oreCount - increment

print(findRawReactants(conversion, 'FUEL'))