from typing import List


def recursiveCombat(first: List[int], second: List[int]):
    """
    this thing returns a tuple
    first element is who won- 1 is p1, 2 is p2
    and the following is the remaining decks of the stuff and yeah
    """
    first = first.copy()  # make sure nothing wonky happens because of list mutability
    second = second.copy()
    seenConfigs = set()
    immediatePrev = (tuple(first), tuple(second))
    while all([first, second]):
        if (tuple(first), tuple(second)) in seenConfigs:
            return 1, first, second
        next1 = first.pop(0)
        next2 = second.pop(0)
        if next1 <= len(first) and next2 <= len(second):
            if recursiveCombat(first[:next1], second[:next2])[0] == 1:
                first.extend([next1, next2])
            else:
                second.extend([next2, next1])
        else:
            if next1 > next2:
                first.extend([next1, next2])
            else:
                second.extend([next2, next1])
        seenConfigs.add(immediatePrev)
        immediatePrev = tuple(first), tuple(second)
    if first:
        return 1, first, second
    else:
        return 2, first, second


with open('giveASmolPhrase.txt') as read:
    p1, p2 = [p.split('\n') for p in read.read().split('\n\n')]
    player1 = [int(c) for c in p1 if c.isdigit()]
    player2 = [int(c) for c in p2 if c.isdigit()]
starting1 = player1.copy()
starting2 = player2.copy()

while all([player1, player2]):
    p1Next = player1.pop(0)
    p2Next = player2.pop(0)
    if p1Next > p2Next:
        player1.extend([p1Next, p2Next])
    else:
        player2.extend([p2Next, p1Next])

winner = player1 if player1 else player2
p1Total = sum((v + 1) * c for v, c in enumerate(reversed(winner)))
print(p1Total)

recursiveResult = recursiveCombat(starting1, starting2)
p2Total = sum((v + 1) * c for v, c in enumerate(reversed(recursiveResult[recursiveResult[0]])))
print(p2Total)
