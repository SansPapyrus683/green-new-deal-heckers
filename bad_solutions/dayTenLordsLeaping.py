from math import sqrt
from sys import exit

asteroids = []
allpts = []
file = open("C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/whoLeaps.txt")
with file as data:
    for v, line in enumerate(data):
        count = 0
        for c in line.rstrip():
            if c == "#":
                asteroids.append([count, v])
                allpts.append([count, v])
            elif c == ".":
                allpts.append([count, v])
                pass
            count += 1

# PART 1
def distance(firstPt, secondPt):
    return sqrt((firstPt[0] - secondPt[0]) ** 2 + (firstPt[1] - secondPt[1]) ** 2)


def findCloset(pt, ptList):
    for ppt in ptList:
        ppt.insert(0, distance(pt, ppt))
    ptList.sort()
    for ppt in ptList:
        ppt.pop(0)
    return ptList


# this slope function is upside down oof
def slope(firstPt, secondPt):
    try:
        slope = -((firstPt[1] - secondPt[1]) / (firstPt[0] - secondPt[0]))
    except ZeroDivisionError:
        slope = float("inf")
    return slope


def checkRange(range, num):
    x = range.copy()
    x.sort()
    if x[0] <= num <= x[1]:
        return True
    return False


count = 0
partOneRun = True
if partOneRun:
    for v, a in enumerate(asteroids):
        # print(a)
        otherAst = asteroids[:v]
        otherAst.extend(asteroids[v + 1 :])
        seen = []
        for ast in findCloset(a, otherAst):
            for aste in seen:
                # print(ast, aste)
                if (
                    slope(a, ast) == slope(a, aste)
                    and checkRange([a[0], ast[0]], aste[0])
                    and checkRange([a[1], ast[1]], aste[1])
                ):
                    break
            else:
                seen.append(ast)
        if len(seen) > count:
            good = a
            count = len(seen)
    print("%s is the optimal asteroid, it can see %i others" % (good, count))

# PART 2
# good for my input was [19,11]
allOthers = asteroids[: asteroids.index(good)]
allOthers.extend(asteroids[asteroids.index(good) + 1 :])
allOthers = findCloset(good, allOthers)
allSlopes = list(set([slope(good, p) for p in allOthers]))
allSlopes.sort(reverse=True)
forRightSide = [x for x in allOthers if x[0] >= good[0]]
forLeftSide = [x for x in allOthers if x[0] <= good[0]]
for v, p in enumerate(forRightSide):
    if p[0] == good[0] and good[1] < p[1]:
        del forRightSide[v]
for v, p in enumerate(forLeftSide):
    if p[0] == good[0] and good[1] > p[1]:
        del forLeftSide[v]
ZapCount = 0
orientationMarker = 0
firstInf = True

betNumber = 200
while forRightSide or forLeftSide:
    if orientationMarker % 2 == 0:
        x = 0
        while x < len(allSlopes):  # for the right half
            s = allSlopes[x]
            for v, p in enumerate(forRightSide):
                if slope(good, p) == s and good[0] <= p[0]:
                    # print('asteroid deletus %s' %p)
                    ZapCount += 1
                    if ZapCount == betNumber:
                        print("here- the elves be stoopid", p)
                    del forRightSide[v]
                    x += 1
                    break
                elif good[0] > p[0]:
                    x = len(allSlopes)
                    break
            else:
                x += 1
        orientationMarker += 1
    elif orientationMarker % 2 == 1:  # for the left half
        x = 0
        while x < len(allSlopes):
            s = allSlopes[x]
            for v, p in enumerate(forLeftSide):
                if slope(good, p) == s and good[0] >= p[0]:
                    # print('asteroid deletus %s' %p)
                    ZapCount += 1
                    if ZapCount == betNumber:
                        print("here- the elves be stoopid", p)
                    del forLeftSide[v]
                    x += 1
                    break
                elif good[0] < p[0]:
                    x = len(allSlopes)
            else:
                x += 1
        orientationMarker += 1
