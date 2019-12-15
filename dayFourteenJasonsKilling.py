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

def findRawReactants(reactionList, element = 'FUEL', alreadyHave = 0, amt = 1):
    """break everything down into ore components
    amt is the amt produced, and alreadyHave is kinda misleading:
    its just if any components (not of ores)"""
    oreCount = 0
    for v, reaction in enumerate(reactionList):
        if reaction[0][-1] == element:

            pass
    return increment, oreCount, alreadyHave