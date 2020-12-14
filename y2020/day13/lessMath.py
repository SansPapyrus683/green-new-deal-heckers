from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def minTime(wantedModulos, searchFrom=0, increment=1):
    if not wantedModulos:
        return searchFrom
    satisfied = wantedModulos[0]
    while searchFrom % satisfied[0] != satisfied[1]:
        searchFrom += increment
    return minTime(wantedModulos[1:], searchFrom, lcm(increment, satisfied[0]))


with open('reallyFly.txt') as read:
    read.readline()
    buses = [int(b) if b.lower() != 'x' else -1 for b in read.readline().rstrip().split(',')]

busesAndMods = [(b, (b - v) % b) for v, b in enumerate(buses) if b != -1]
print("boy this method was so much simpler lol: %i" % minTime(busesAndMods))
