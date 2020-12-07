def contains(allBags, start, end):
    for _, subbag in allBags[start]:
        if subbag == end or contains(allBags, subbag, end):
            return True


def bagNumber(allBags, theBag):
    totalNum = 0
    for bagNum, subBag in allBags[theBag]:
        # we need the bagNum of the subbag and then bagNum of each of the sub-subbags, and so on
        totalNum += bagNum + bagNum * bagNumber(allBags, subBag)
    return totalNum


with open('seasons.txt') as read:
    bags = {}
    for line in read.readlines():
        line = line.strip().split(' contain ')

        # NOTE: the bags has to come before bag (or else you end up with a buncha random s chars)
        for extraneous in ['bags', 'bag', 'no other', '.']:
            line = [s.replace(extraneous, '').strip() for s in line]

        outside, inside = line  # just being a explicit here
        inside = [i.strip().split() for i in inside.split(',') if i.strip()]

        bags[outside] = [[int(b[0]), " ".join(b[1:])] for b in inside]

myBag = "shiny gold"
containsMyBag = 0
for b in bags:
    if b != myBag and contains(bags, b, myBag):
        containsMyBag += 1
print("goddamn the string parsing for this problem was hell: %i" % containsMyBag)
print("but boy i have improved on my recursion skills in a year tho: %i" % bagNumber(bags, myBag))
