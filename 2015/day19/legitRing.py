from collections import defaultdict

def splitAtoms(molecule):
    composition = []
    buildUp = []
    first = True
    for c in molecule:
        if first:
            buildUp.append(c)
            first = False
            continue
        if c.upper() == c:
            composition.append(''.join(buildUp))
            buildUp = []
        buildUp.append(c)

    if buildUp:
        composition.append(''.join(buildUp))
    return composition


conversion = defaultdict(lambda: [])
convBack = []
with open('notPhone.txt') as read:
    detectingConversions = True
    for line in read.readlines():
        if line == '\n':
            detectingConversions = False
        if detectingConversions:
            line = line.rstrip().replace(' => ', ' ').split()
            conversion[line[0]].append(splitAtoms(line[1]))
            convBack.append([line[1], splitAtoms(line[0])])  # for part 2
        else:
            medMol = splitAtoms(line.rstrip())

possible = set()
for v, a in enumerate(medMol):
    for replacement in conversion[a]:
        if ''.join(medMol[:v] + replacement + medMol[v + 1:]) not in possible:
            possible.add(''.join(medMol[:v] + replacement + medMol[v + 1:]))

print('but what if i don\'t want to save rudolph: %i' % len(possible))

print("i would just leave rudolph for dead but here: %i"
      % (len(medMol) - (medMol.count('Rn') + medMol.count('Ar')) - 2 * (medMol.count('Y')) - 1))

# followed u/askalski's sol on Reddit: https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/
# TODO: actually understand this crap
