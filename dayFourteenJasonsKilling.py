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
def findRawReactants(reactionList, element = 'FUEL', alreadyHave = 0, amt = 1):
    """break everything down into ore components"""
    oreCount = 0
    leftOverOre = 0
    for v, reaction in enumerate(reactionList):
        if reaction[0][1] == element:
            increment = reaction[0][0]
            #print(increment)
            if reaction[1][1] == 'ORE': #its only ore when its used
                production = amt//reaction[1][0] + 1
                for i in range(production):
                    while reaction[1][0] <= alreadyHave:
                        alreadyHave -= reaction[1][0]
                    else:
                        oreCount += reaction[1][0]                                                                      
                #print('current orecount',oreCount)
                return increment, oreCount, alreadyHave
            else:
                print(reaction)
                for el in reaction[1:]:
                    x = findRawReactants(reactionList[:v] + reactionList[v + 1:], el[1], alreadyHave)
                    oreCount += x[1]
                    print('asdf',x)
                    print('Orecount for element %s: %s but it left over %s' %(el, x[1], x[2]))
                    leftOverOre = x[2]
                    print('storage: %s' % leftOverOre)
    return increment, oreCount, oreCount - leftOverOre

print('horrible output ->',findRawReactants(conversion, 'C'))