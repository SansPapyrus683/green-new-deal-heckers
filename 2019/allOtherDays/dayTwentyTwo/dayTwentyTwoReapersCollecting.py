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
shuffleTimes = 101741582076661


def composeFunc(firstCo, secondCo, cardModulo=deckLength):
    return (firstCo[0] * secondCo[0]) % cardModulo, (firstCo[1] * secondCo[0] + secondCo[1]) % cardModulo


def inv(a, n):  # copying code is a wonderful thing
    return pow(a, n - 2, n)


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

print('so this is the coefficients that when plugged in, equate to one shuffle: %s, %s' % initialCo)
bigA = pow(initialCo[0], shuffleTimes, deckLength)
bigB = (initialCo[1] * (bigA - 1) * inv(initialCo[0] - 1, deckLength)) % deckLength
print('so this coefficient equate to the pos of a card after a huge amt of shuffles: %s, %s' % (bigA, bigB))

print('if you ENJOYED this day then you should check in at the mental ward: %i'
      % (((2020 - bigB) * inv(bigA, deckLength)) % deckLength))
