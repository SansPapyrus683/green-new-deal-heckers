from copy import deepcopy

auntReading = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5,
               'trees': 3, 'cars': 2, 'perfumes': 1}
otherAunts = {}
with open('whatAbtMe.txt') as read:
    for v, line in enumerate(read):
        line = line.rstrip()[line.find(':') + 2:]
        things = {}
        for trait in line.split(sep=', '):
            things[trait[:trait.find(':')]] = int(trait[trait.find(':') + 1:])
        otherAunts[v + 1] = things

suspects = deepcopy(otherAunts)  # PART 1
for a in otherAunts:
    for trait in otherAunts[a]:
        if auntReading[trait] != otherAunts[a][trait]:
            del suspects[a]  # eliminate the suspect if it doesn't conform to the original requirements
            break

print("i don't remember having any aunt sues...: %i" % list(suspects.keys())[0])

suspects = deepcopy(otherAunts)  # PART 2
for a in otherAunts:
    for trait in otherAunts[a]:
        if trait in ['cats', 'trees']:
            if auntReading[trait] >= otherAunts[a][trait]:  # p much the same thing as part 1
                del suspects[a]
                break
        elif trait in ['pomeranians', 'goldfish']:
            if auntReading[trait] <= otherAunts[a][trait]:
                del suspects[a]
                break
        else:
            if auntReading[trait] != otherAunts[a][trait]:
                del suspects[a]
                break

print("ah yes, i do indeed enjoy treating people like numbers: %i" % list(suspects.keys())[0])
