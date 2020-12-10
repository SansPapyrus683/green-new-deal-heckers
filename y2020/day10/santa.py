MAX_DIFF = 3

with open('onHisWay.txt') as read:
    adapters = sorted(set(int(line) for line in read.readlines()))

adapters.append(adapters[-1] + 3)  # add the built-in joltage adapter and the wall adapter
adapters.insert(0, 0)
oneDiffNum = 0
threeDiffNum = 0
prev = 0
for a in adapters:
    if a - prev == 1:
        oneDiffNum += 1
    elif a - prev == 3:
        threeDiffNum += 1
    prev = a
print("jesus christ why does the protag have so many adapters: %i" % (oneDiffNum * threeDiffNum))

# this[i] = amt of ways given that we use adapters[i]
combsSoFar = [0 for _ in range(len(adapters))]
combsSoFar[0] = 1
for i in range(1, len(adapters)):
    for a in range(max(0, i - MAX_DIFF), i):
        if adapters[a] + MAX_DIFF >= adapters[i]:
            combsSoFar[i] += combsSoFar[a]

# we have to end at the built-in adapter, so just take the last element
print("were they preparing for like a worldwide adapter shortage or something: %i" % combsSoFar[-1])
