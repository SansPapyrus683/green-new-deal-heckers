from collections import defaultdict
# oh i got snowdin in my input
# THAT'S A GOSH DARN UNDERTALE REFERENCE
# YEAAAAAAA
distances = defaultdict(lambda: defaultdict(lambda: float('inf')))
with open('notALot.txt') as read:
    for line in read.readlines():
        line = line.replace(' to ', ' ')  # makes processing easier
        line = line.replace(' = ', ' ')
        distances[line.split()[0]][line.split()[1]] = distances[line.split()[1]][line.split()[0]] = int(line.split()[2])
    distances = {c: dict(distances[c]) for c in distances}  # makes it more readable if u wanna see it

possVisits = [[[p], 0] for p in distances]  # santa's path & distance travelled
for _ in range(len(distances) - 1):  # do a bfs
    inLine = []
    for state in possVisits:  # state of being, not actual state lol
        for n in distances[state[0][-1]]:
            if n not in state[0]:  # don't visit a place twice
                inLine.append([state[0] + [n], state[1] + distances[state[0][-1]][n]])
    possVisits = inLine

print('i thought it was prim\'s at first lol :%i' % min([a[-1] for a in possVisits]))
print('santa is contributing to global warming by taking the longest path: %i' % max([a[-1] for a in possVisits]))
