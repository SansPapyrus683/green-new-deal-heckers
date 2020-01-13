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

N = 10**10000000000000000
def exponentiation(bas, exp):
    t = 1
    while exp > 0:
        if exp % 2 != 0:
            t = (t * bas) % N

        bas = (bas * bas) % N
        exp = int(exp / 2)
    return t % N

print(exponentiation(10*12, 10*12))

initialCo = (1, 0)
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
print(exponentiation(10001234, 1000000000))
