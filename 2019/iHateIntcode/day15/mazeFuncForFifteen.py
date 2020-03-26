"""all this is just for day 15
because it technically counts as an intcode challenge"""


def findNeighbors(pt: "point", ptList: "list of good points") -> set:
    possibleNeighbors = {
        (pt[0] - 1, pt[1]),
        (pt[0] + 1, pt[1]),
        (pt[0], pt[1] - 1),
        (pt[0], pt[1] + 1),
    }
    return possibleNeighbors.intersection(ptList)


def manhattan(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


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
