"""ill be putting all my bfs & find neighbors stuff here
ill update d15 later, because im that lazy"""
from heapq import heappush, heappop


def findNeighbors(pt: "point", ptList: "list of good points") -> set:
    possibleNeighbors = {
        (pt[0] - 1, pt[1]),
        (pt[0] + 1, pt[1]),
        (pt[0], pt[1] - 1),
        (pt[0], pt[1] + 1),
    }
    return possibleNeighbors.intersection(ptList)


def manhattan(a, b) -> int:
    """shameless copied from some place other than stackoverflow
    they called me a madman"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def goToPos(start, ptList, goal) -> (int, list):
    # path that goes to the thing along with the amt of moves needed
    tempFrontier = [(0, start)]
    cameFromPos = {start: None}  # pycharm told me to do this
    costSoFar = {start: 0}

    while tempFrontier:
        processed = heappop(tempFrontier)[1]

        if processed == goal:
            break

        for nextPt in findNeighbors(processed, ptList):
            newCost = costSoFar[processed] + 1
            if nextPt not in costSoFar or newCost < costSoFar[nextPt]:
                costSoFar[nextPt] = newCost
                priority = newCost + manhattan(nextPt, goal)
                heappush(tempFrontier, (priority, nextPt))
                cameFromPos[nextPt] = processed

    processed = goal
    path = set()
    while processed != start:
        path.add(processed)
        processed = cameFromPos[processed]

    return len(path), path


def justDistance(start, ptList, goal) -> int:
    frontier = {start}
    visited = {start}
    moveCount = 0
    while frontier:
        inLine = set()
        for pt in frontier:
            for p in findNeighbors(pt, ptList):
                if p not in visited:
                    inLine.add(p)
                visited.add(p)

        moveCount += 1
        frontier = inLine
        if goal in frontier:
            return moveCount


def findKeys(alreadyHave, keyRequirement):
    """takes a bunch of keys and returns the keys you can get
    in case you couldn't tell, this was just for d18"""
    canGet = []
    alreadyHave = set(alreadyHave)  # better do this once, rather than in a loop
    for required in keyRequirement:
        if (
                set(keyRequirement[required]).issubset(alreadyHave)
                and required not in alreadyHave
        ):
            canGet.append(required)
    return canGet


ptsAndWormholes = {}


def wormholeNeighbors(pt, ptList, linkedPts: dict):
    possibleNeighbors = {
        (pt[0] - 1, pt[1]),
        (pt[0] + 1, pt[1]),
        (pt[0], pt[1] - 1),
        (pt[0], pt[1] + 1),
    }
    goodNeighbors = possibleNeighbors.intersection(ptList)
    for value in linkedPts.values():
        if pt in value:
            goodNeighbors.add(value[not value.index(pt)])
    return goodNeighbors


def wormholeDistance(start, ptList, goal, wormholePts) -> int:
    frontier = {start}
    visited = {start}
    moveCount = 0
    while frontier:
        inLine = set()
        for pt in frontier:
            for p in wormholeNeighbors(pt, ptList, wormholePts):
                if p not in visited:
                    inLine.add(p)
                visited.add(p)

        moveCount += 1
        frontier = inLine
        if goal in frontier:
            return moveCount


if __name__ == '__main__':
    testPts = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4), (4, 2)]
    print(justDistance((0, 0), testPts, (3, 3)))
    print(goToPos((0, 0), testPts, (3, 3)))
    print(findNeighbors((0, 0), [(0, 1), (1, 0)]))
    print(findKeys({'a', 'b'}, {'c': ['a', 'b'], 'a': [], 'b': ['a']}))
