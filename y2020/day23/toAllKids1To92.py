from typing import List


class Cup:
    def __init__(self, val: int, next_: "Cup" = None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return f"Cup{{val={self.val},nextVal={self.next.val}}}"

    def trav(self, amt: int):
        val = self.next
        for _ in range(amt - 1):
            val = val.next
        return val


def simulate(circle: List[Cup], amt: int = 100):
    curr = circle[0]
    highest = max(c.val for c in circle)
    circle.sort(key=lambda c: c.val)  # make it a list of the values to indices (off by one, keep that in mind)
    for _ in range(amt):
        taken = [curr.next, curr.trav(2), curr.trav(3)]
        noNoVals = [c.val for c in taken]

        destination = highest if curr.val == 1 else curr.val - 1
        while destination in noNoVals:
            destination = highest if destination == 1 else destination - 1

        curr.next = curr.trav(4)
        insertAfter = circle[destination - 1]
        taken[-1].next = insertAfter.next
        insertAfter.next = taken[0]
        curr = curr.next
    return circle


def order(circle: List[Cup]):
    start = circle[0]
    pos = circle[0]
    result = str(pos.val)
    while pos.next != start:
        pos = pos.next
        result += str(pos.val)
    return result


cups = [int(i) for i in "467528193"]

p1Cups = [Cup(c) for c in cups]
for i in range(len(p1Cups)):
    p1Cups[i].next = p1Cups[(i + 1) % len(p1Cups)]
simulate(p1Cups, 100)
print("ngl i kinda want to kill this crab: %s" % order(p1Cups)[1:])

p2Cups = [Cup(c) for c in cups + [i for i in range(max(cups) + 1, 10 ** 6 + 1)]]
for i in range(len(p2Cups)):
    p2Cups[i].next = p2Cups[(i + 1) % len(p2Cups)]
simulate(p2Cups, 10 ** 7)
cup1 = p2Cups[0]
print("where did the crab even get all those cups lol: %i" % (cup1.next.val * cup1.trav(2).val))
