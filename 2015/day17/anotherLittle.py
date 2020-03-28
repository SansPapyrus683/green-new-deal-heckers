from itertools import combinations

containers = []
with open('actuallySmall.txt') as read:
    for line in read.readlines():
        containers.append(int(line.rstrip()))

combCount = 0
spikedEggs = 150
allArrangements = []
for i in range(1, len(containers) + 1):
    for cups in combinations(containers, i):  # try all possible combinations
        if sum(cups) == 150:  # it actually doesn't take that much time
            allArrangements.append(cups)
            combCount += 1

print("how much did that amt of eggnog cost anyways: %i" % combCount)
print("and santa should've fired the elves that bought the eggnog imo: %i"
      % len([c for c in allArrangements if len(c) == min([len(co) for co in allArrangements])]))
