from itertools import permutations

totalArea = 0
totalRibbons = 0

with open('goodBoy.txt') as read:
    for l in read.readlines():
        l = [int(x) for x in l.rstrip().split(sep='x')]
        faceList = []
        pList = []
        for face in permutations(l, 2):  # permutations bc each face has to be counted twice
            faceList.append(face[0] * face[1])
            pList.append(2 * face[0] + 2 * face[1])

        boxRibbons = min(pList) + l[0] * l[1] * l[2]
        faceList.append(min(faceList))  # the little "extra"- i think they're just secretly hoarding the paper there

        totalArea += sum(faceList)  # add the final sums to the total count
        totalRibbons += boxRibbons

print(totalArea, 'darn thats alot of paper- #TEAMTREES GUYS')  # part 1
print(totalRibbons, 'how does santa\'s business even stay afloat')  # part 2
