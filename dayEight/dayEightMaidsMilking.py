def chunks(lst, n):
    """Yield successive n-sized chunks from lst. shamless copied from
    stack overflow lol"""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]

with open(
    "C:/Users/kevin/Documents/GitHub/green-new-deal-heckers/data stuff/milkFlashback.txt"
) as data:
    for line in data.readlines():
        # PART 1
        line = line.rstrip()
        width = 25
        height = 6
        puzzle = [int(x) for x in list(line)]
        currIndex = 0
        layers = []
        for i in range(len(puzzle) // (width * height)):
            layers.append(puzzle[currIndex : width * height + currIndex])
            currIndex += width * height
        lowestZeroes = float("inf")
        for layer in layers:
            count = 0
            for i in layer:
                if i == 0:
                    count += 1
            if count < lowestZeroes:
                lowestLayer = layer
                lowestZeroes = count
        oneCount, twoCount = 0, 0
        for i in lowestLayer:
            if i == 1:
                oneCount += 1
            elif i == 2:
                twoCount += 1
        print(oneCount * twoCount)

# PART 2
final = []
layerCopy = layers.copy()
zippedLayers = zip(*layerCopy)

for i in zippedLayers:
    for z in i:
        if z == 1:
            final.append(1)
            break
        elif z == 0:
            final.append(0)
            break
print(final)
written = open("test.txt", "w")
for l in chunks(final, 25):
    for i in l:
        if i == 1:
            print("||", end="")
        else:
            print("  ", end="")
    print("\n", end="")
