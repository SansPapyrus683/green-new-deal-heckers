from itertools import permutations
from collections import defaultdict

happyThoughts = defaultdict(lambda: {})
with open('whatsADuplex.txt') as read:
    for line in read.readlines():
        line = line.rstrip().replace(' would ', ' ')[:-1].replace(' happiness units by sitting next to ', ' ').split()
        if 'gain' in line:
            happyThoughts[line[0]][line[3]] = int(line[2])
        elif 'lose' in line:
            happyThoughts[line[0]][line[3]] = -1 * int(line[2])
    happyThoughts = dict(happyThoughts)

def happyTable(setup):
    happinessMeter = {p: 0 for p in happyThoughts}
    for v, p in enumerate(setup):
        if v == (len(setup) - 1):
            happinessMeter[p] = happyThoughts[p][setup[v - 1]] + happyThoughts[p][setup[0]]
        else:
            happinessMeter[p] = happyThoughts[p][setup[v-1]] + happyThoughts[p][setup[v+1]]
    return sum(happinessMeter.values())

print('jokes on you-i don\'t eat with anyone during christmas. it\'s just me... all alone... with my ice cream...: %s' %
      max([happyTable(comb) for comb in permutations(happyThoughts.keys())]))

happyThoughts['me'] = {p: 0 for p in happyThoughts}
for person in happyThoughts:
    happyThoughts[person]['me'] = 0

print('do i really have to eat with everyone else? i just wanna play video games and be alone: %s' %
      max([happyTable(comb) for comb in permutations(happyThoughts.keys())]))
