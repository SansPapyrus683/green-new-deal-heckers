food = []
numAt = 0
allAllergens = set()
allIngredients = set()
with open('reallyKnowHowToFly.txt') as read:
    for line in read.readlines():
        line = line.strip()
        ingredients = [i.strip() for i in line[:line.find('(')].split()]
        allergens = [i.strip() for i in line[line.find('(') + 1:-1].replace('contains', '').split(',')]
        for a in allergens:
            allAllergens.add(a)
        for i in ingredients:
            allIngredients.add(i)
        food.append([ingredients, allergens])

toxins = set()
possibleList = {}
for a in allAllergens:
    shared = allIngredients.copy()
    for f in food:
        if a in f[1]:
            shared = shared.intersection(f[0])
    toxins = toxins.union(shared)
    possibleList[a] = shared

safeCount = 0
for f in food:
    for i in f[0]:
        if i not in toxins:
            safeCount += 1
print("good god what kind of a language is this: %i" % safeCount)

canonical = {a: '' for a in allAllergens}
while not all(canonical.values()):
    for a, i in possibleList.items():
        if len(i) == 1:
            canonical[a] = i.pop()
            for other in possibleList.values():
                if canonical[a] in other:
                    other.remove(canonical[a])
print("and why does the protag have so many allergies lol: %s" % ','.join(canonical[a] for a in sorted(allAllergens)))
