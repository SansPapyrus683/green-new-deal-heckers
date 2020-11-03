from collections import Counter
codes = []
with open("theyreGlowing.txt") as read:
    for l in read.readlines():
        codes.append(l.rstrip())

p1message = ""
p2message = ""
for c in zip(*codes):
    most_often = Counter(c).most_common()
    p1message += most_often[0][0]
    p2message += most_often[-1][0]

print("the heck is santa trying to tell us through \"%s\"?" % p1message)
print("i mean does the protagonist know something i don't: %s" % p2message)
