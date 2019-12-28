from sys import exit  # just for debugging

orbits = []
with open("C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/geeseEggs.txt") as eggs:
    for line in eggs.readlines():
        orbits.append(
            [s for s in line.rstrip().split(sep=")")]
        )  # the thing being orbited, the orbiter

plantes = []
for o in orbits:
    for x in o:
        if x not in plantes:
            plantes.append(x)

# PART 1
def orbitNumber(planet, orbitList):
    orbiteeNumber = 0
    orbiteeNumber += len(orbitList[planet])
    for pl in orbitList[planet]:
        if pl in orbited:
            # print(pl)
            orbiteeNumber += orbitNumber(pl, orbitList)
        # i mean if nothing orbits it it doesnt matter
    return orbiteeNumber


newOrbits = {}  # orbited: orbitees
for v, o in enumerate(orbits):
    tempOrbitList = o[1:]
    for ob in orbits[:v] + orbits[v + 1 :]:
        if ob[0] == o[0]:
            tempOrbitList.extend(ob[1:])
    newOrbits[o[0]] = tempOrbitList
# 251208
# print(newOrbits)
realCount = 0
orbited = [ob for ob in newOrbits]

for ob in orbited:
    realCount += orbitNumber(ob, newOrbits)

print("our checksum is %i - is that valid?" % realCount)

# PART 2
def findPath(planet, orbitList):
    path = []
    for o in orbitList:
        if planet in orbitList[o]:
            path.append(o)
        if not path:
            continue
        elif "COM" not in path:
            path.extend(findPath(path[-1], orbitList))
        elif "COM" in path:
            return path


for k in newOrbits:
    if "YOU" in newOrbits[k]:
        whereUAt = k
    elif "SAN" in newOrbits[k]:
        whereHeAt = k

yourPath = findPath(whereUAt, newOrbits)
santaPath = findPath(whereHeAt, newOrbits)
lowestScore = float("inf")
for v, pl in enumerate(yourPath):
    for x, pla in enumerate(santaPath):
        if pl == pla:
            if v + x + 2 < lowestScore:
                lowestScore = v + x + 2
print("the min amt of orbital transfers  is %i" % lowestScore)
