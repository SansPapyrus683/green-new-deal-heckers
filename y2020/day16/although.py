requirements = []
theirs = []
reqNum = 0
wantedReqs = []
with open('itHasBeenSaidTho.txt') as read:
    state = None
    for line in read.readlines():
        line = line.strip()
        if line == 'your ticket:':  # this parsing is really hacky but hey, perfect input!
            state = False

        elif line == 'nearby tickets:':
            state = True

        elif ':' in line:
            if line.startswith('departure'):
                wantedReqs.append(reqNum)
            line = [r.strip() for r in line[line.find(':') + 1:].split('or')]
            reqs = []
            for r in line:
                reqs.append([int(i) for i in r.split('-')])
            requirements.append(reqs)
            reqNum += 1

        elif ',' in line:
            if state is not None and not state:
                mine = [int(i) for i in line.split(',')]
            else:
                theirs.append([int(i) for i in line.split(',')])
assert len({len(t) for t in theirs}) == 1, 'all tickets should be consistent my guy'

validTickets = []
errorRate = 0
for t in theirs:
    overallValid = True
    for field in t:
        if not any(any(range_[0] <= field <= range_[1] for range_ in req) for req in requirements):
            errorRate += field
            overallValid = False
    if overallValid:
        validTickets.append(t)
print("where did we have the time to write down so many tickets lol: %i" % errorRate)

possible = [[] for _ in range(len(validTickets[0]))]
for v, r in enumerate(requirements):
    for i in range(len(validTickets[0])):
        # if all of the numbers in row i satisfy the range requirements, add it
        if all(any(range_[0] <= t[i] <= range_[1] for range_ in r) for t in validTickets):
            possible[i].append(v)

assigned = [None for _ in range(len(validTickets[0]))]
while any(a is None for a in assigned):
    for v, p in enumerate(possible):
        if len(p) == 1:  # ok, we've narrowed it down to a single possibility
            toAssign = p[0]
            assigned[v] = toAssign
            for other in possible:
                if toAssign in other:
                    other.remove(toAssign)

prod = 1
for v, a in enumerate(assigned):
    if a in wantedReqs:
        prod *= mine[v]
print("and maybe you could just ask one of the locals who's bilingual too- BRUH the protag is dumb as frick: %i" % prod)
