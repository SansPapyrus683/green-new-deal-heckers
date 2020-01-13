"""somebody's going to die tonight"""

with open('grimReaper.txt') as shuffles:
    trickList = [l.rstrip() for l in shuffles.readlines()]

# PART 1
def cheapShuffle(targetCardPos, cardNumber):
    for localTrick in trickList:
        if localTrick.startswith('deal into'):
            targetCardPos = (cardNumber - targetCardPos - 1) % cardNumber
        elif localTrick.startswith('deal with'):
            dealAmt = int(localTrick[20:])
            targetCardPos = (dealAmt * targetCardPos) % cardNumber
        elif localTrick.startswith('c'):
            cut_amt = int(localTrick[4:])  # the black sheep out of all the other vars
            targetCardPos = (targetCardPos - cut_amt) % cardNumber
    return targetCardPos

print('who is this \'you\' and why is he THIS bored: %s' % cheapShuffle(2019, 10007))

# PART 2 CAN GO DIE IN A HOLE
# so i followed this tutorial: https://codeforces.com/blog/entry/72593 its kinda complicated
deckLength = 119315717514047

def composeFunc(firstCo, secondCo, cardModulo=deckLength):
    return (firstCo[0] * secondCo[0]) % cardModulo, (firstCo[1] * secondCo[0] + secondCo[1]) % cardModulo

initialCo = (1, 0)  # all the shuffles can be categorized as: f(x) = initialCo[0] * x * initialCoo[1], where x is the
# position of the card (it tells what position the card ends up at)
for trick in trickList:
    if trick.startswith('deal into'):
        initialCo = composeFunc(initialCo, (-1, -1))
    elif trick.startswith('deal with'):
        dealIncrement = int(trick[20:])
        initialCo = composeFunc(initialCo, (dealIncrement, 0))
    elif trick.startswith('c'):
        cutAmt = int(trick[4:])
        initialCo = composeFunc(initialCo, (1, -1 * cutAmt))

print(initialCo)
print((initialCo[0] * 2020 + initialCo[1]) % deckLength)
finalCo = (initialCo[0] ** deckLength, (initialCo[1] * (1 - initialCo[0] ** deckLength))/(1 - initialCo[0]))
print(finalCo)
