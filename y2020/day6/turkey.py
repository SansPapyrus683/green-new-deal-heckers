with open('mistletoe.txt') as read:
    soFar = []
    allAnswers = []
    for line in read.readlines():
        if line == '\n':
            allAnswers.append(soFar)
            soFar = []
        else:
            soFar.append(line.strip())
    allAnswers.append(soFar)

p1Total = 0
p2Total = 0
for a in allAnswers:
    everyone = set(a[0])
    for p in a[1:]:
        everyone = everyone.intersection(set(p))
    p2Total += len(everyone)
    p1Total += len(set(''.join(a)))
print("the premise of this problem is really weird ngl%i" % p1Total)
print("and there were only what, 1000 seats on the plane from day 5? how the frick-%i" % p2Total)
