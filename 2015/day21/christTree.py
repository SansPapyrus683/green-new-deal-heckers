from itertools import combinations
# i hate hardcoding but file processing isn't the most attractive option either
weapons = [[8, 4, 0],
           [10, 5, 0],
           [25, 6, 0],
           [40, 7, 0],
           [74, 8, 0]]

armor = [[13, 0, 1],
         [31, 0, 2],
         [53, 0, 3],  # cost, damage, armor
         [75, 0, 4],
         [102, 0, 5]]
# idk if your shop is different but sorry if you wanna run your input into mine and our shops are different
rings = [[25, 1, 0],
         [50, 2, 0],
         [100, 3, 0],
         [20, 0, 1],
         [40, 0, 2],
         [80, 0, 3]]

boss = []
with open('star.txt') as read:
    for v, line in enumerate(read):
        boss.append(int(line[line.find(':') + 1:]))

def attack(offender, defender):  # [HP, damage, armor]
    damage = offender[1] - defender[2] if offender[1] - defender[2] > 0 else 1
    defender[0] -= damage  # no need to return anything, because lists are mutable

def bossFight(stats):
    myStats = [100] + stats
    bossStats = boss.copy()
    whoseTurn = True  # True = my turn, False = boss's turn
    while not (myStats[0] <= 0 or bossStats[0] <= 0):
        if whoseTurn:
            attack(myStats, bossStats)
        else:
            attack(bossStats, myStats)
        whoseTurn = not whoseTurn

    if myStats[0] <= 0:
        return False
    return True

# get all the stat combinations- this took more code than i thought
armorComb = [[0, 0, 0]] + armor  # [0,0,0] is no armor pretty much
ringComb = []
for i in range(3):  # get all combinations of rings
    for c in combinations(rings, i):
        ringComb.append(list(c))

gearComb = [w for w in weapons]
for g in [armorComb, ringComb]:
    inLine = []
    for c in gearComb:  # do a bfs of all gear states? idk
        for gear in g:
            if g == armorComb:
                inLine.append([c, gear])
            else:
                inLine.append(c + gear)
    gearComb = inLine

statComb = []
for comb in gearComb:
    statComb.append([sum([g[i] for g in comb]) for i in range(3)])


statComb.sort()
for s in statComb:
    if bossFight(s[1:]):
        print('this is a HORRIBLE game. zero stars. : %i' % s[0])
        break

for s in reversed(statComb):
    if not bossFight(s[1:]):
        print("how come henry is so easily appeased by these trivial games: %i" % s[0])
        break
