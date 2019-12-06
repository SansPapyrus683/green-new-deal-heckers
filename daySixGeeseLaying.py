orbits = []
with open('geeseEggs.txt') as eggs:
    for line in eggs.readlines():
        orbits.append([s for s in line.rstrip().split(sep = ')')]) #the thing being orbited, the orbiter

plantes = []
for o in orbits:
    for x in o:
        if x not in plantes:
            plantes.append(x)

#PART 1
def calculateOrbits(planet, orbitList):
    orbitedList = [i[0] for i in orbitList]
    orbiteeList = []
    #print(orbitedList)
    for sl in orbitList:
        if sl[0] == planet:
            orbiteeList.extend(sl[1:])
            for pl in sl[1:]:
                #print(pl, orbitedList)
                if pl in orbitedList:
                    #print(pl)
                    orbiteeList.extend(calculateOrbits(pl, orbitList))
            else:
                return orbiteeList
    return set(orbiteeList)
            
newOrbits = [] #heres the struct for a single element: [orbitedPlanet, *insert planets that directly orbit*]
for v, o in enumerate(orbits):
    o = o[0]
    temporaryOrbitList = [o]
    for ob in orbits:
        if ob[0] == o:
            temporaryOrbitList.append(ob[1])
    if len(temporaryOrbitList) > 1:
        newOrbits.append(temporaryOrbitList)

#print(newOrbits)
realCount = 0
orbited = set(ob[0] for ob in newOrbits)
for ob in orbited:
    realCount += len(calculateOrbits(ob, newOrbits))
print(realCount)