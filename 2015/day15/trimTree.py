from copy import deepcopy

ingredients = {}
with open('tiffanyJewlery.txt') as read:
    for line in read.readlines():
        line = line.rstrip().replace(' capacity ', ' ').replace(', durability ', ' ').replace(', flavor ', ' ')
        line = line.replace(', texture ', ' ').replace(', calories ', ' ').split()
        ingredients[line[0][:-1]] = [int(x) for x in line[1:]]

arrangements = [[(list(ingredients.keys())[0], i)] for i in range(0, 101)]
addList = list(ingredients.keys())[1:]
for v, toAdd in enumerate(addList):  # bfs to reach all possible cookie arrangements
    inLine = []
    for a in arrangements:
        usedUp = sum([ig[1] for ig in a])
        if v == len(addList) - 1:
            inLine.append((a + [(toAdd, 100 - usedUp)]))
        else:
            for i in range(100 - usedUp):
                inLine.append((a + [(toAdd, i)]))
    arrangements = inLine


def cookieScore(inArr):  # short for: ingredient arrangement
    thisCookie = deepcopy(ingredients)
    for co in thisCookie:
        for ing in inArr:
            if ing[0] == co:
                for v, p in enumerate(thisCookie[co]):
                    thisCookie[co][v] *= ing[1]  # multiply the ingredient amount first

    properties = []
    for p in range(5):
        pSum = sum([ing[p] for ing in thisCookie.values()])
        if pSum > 0:  # actually calculating the score
            properties.append(sum([ing[p] for ing in thisCookie.values()]))
        else:
            properties.append(0)  # don't worry, calories can't be less than 0

    score = 1
    for v, p in enumerate(properties):
        if v != 4:  # filter out the calories
            score *= p

    return [score, properties[-1]]

allScores = []
for c in arrangements:
    allScores.append(cookieScore(c))

print("i don't think that's how cookies work but ok: %i" % max(allScores)[0])
print("500 calories is definitely alot: %i" % max([c[0] for c in allScores if c[1] == 500]))
