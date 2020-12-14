# plagiarized from https://www.geeksforgeeks.org/chinese-remainder-theorem-set-2-implementation/ lol
def inv(a, m):
    """
    i think this computes the modular inverse of a mod m
    """
    m0 = m
    x0 = 0
    x1 = 1

    if m == 1:
        return 0
    while a > 1:  # so this is the extended euclidean algo?
        q = a // m
        t = m

        m = a % m
        a = t

        t = x0
        x0 = x1 - q * x0
        x1 = t
    # always return a positive value
    return x1 + m0 if x1 < 0 else x1


def findMinX(divisors, remainders):
    """
    ok so given an array num an array num
    this function calcs the min x so that x % num[i] == rem[i] for all the i's
    """
    assert len(divisors) == len(remainders), 'you know what you did wrong buddy'
    prod = 1
    for i in range(len(divisors)):
        prod *= divisors[i]
    result = 0
    for i in range(len(divisors)):
        pp = prod // divisors[i]  # haha can't believe they used pp as a variable name
        result += remainders[i] * inv(pp, divisors[i]) * pp
    return result % prod


with open('reallyFly.txt') as read:
    earliestDepTime = int(read.readline())
    buses = [int(b) if b.lower() != 'x' else -1 for b in read.readline().rstrip().split(',')]

timeAt = earliestDepTime
found = False
while True:
    for b in buses:
        if b == -1:
            continue
        if timeAt % b == 0:
            print("bruh why are so many buses out of service: %i" % ((timeAt - earliestDepTime) * b))
            found = True
            break
    if found:
        break
    timeAt += 1

minBusTime = findMinX([b for b in buses if b != -1], [(b - v) % b for v, b in enumerate(buses) if b != -1])
print("boy it is a very good thing that python has builtin bigint handling: %i" % minBusTime)
