"""im too lazy to put everything in a function"""
from itertools import combinations

packages = set()
with open('joeMomma.txt') as read:
    for line in read.readlines():
        packages.add(int(line.rstrip()))

desiredWeight = sum(packages)//4  # PART 2
validFirstGroups = []
foundMinLen = False
for i in range(1, len(packages)):
    if foundMinLen:
        break
    for arrangement in combinations(packages, i):
        if sum(arrangement) == desiredWeight:
            for x in range(1, len(packages) - i):  # continue checking if the last two can be balanced
                for second in combinations(packages.intersection(set(arrangement)), x):
                    if sum(second) == desiredWeight:
                        for y in range(1, len(packages) - i - x):
                            for third in combinations(packages.intersection(set(arrangement).union(set(second))), y):
                                if sum(third) == desiredWeight:
                                    validFirstGroups.append(arrangement)
                                    foundMinLen = True

bestAmt = min([len(g) for g in validFirstGroups])
topContenders = [g for g in validFirstGroups if len(g) == bestAmt]
quantums = {}
for g in topContenders:
    entanglement = 1
    for pack in g:
        entanglement *= pack
    quantums[g] = entanglement

print('but hey, you\'re looking at someone who doesn\'t even think to put their crap in functions: %i'
      % quantums[[g for g in topContenders if quantums[g] == min(quantums.values())][0]])
