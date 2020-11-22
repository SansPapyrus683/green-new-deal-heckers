BOT_NUM = 250  # gotten from skimming my puzzle input, change them as you wish
OUTPUT_NUM = 25

instructions = []
initialGivens = []
with open('itllBeSomewhere.txt') as read:
    for li in read.readlines():
        li = [w for w in li.rstrip().split() if w not in ["bot", "value", "and", "to", "gives", "goes", "low", "high"]]
        if len(li) == 2:
            initialGivens.append([int(i) for i in li])
        else:
            for i in range(len(li)):
                li[i] = int(li[i]) if li[i].isdigit() else li[i]
            instructions.append(li + [0])  # boolean for if it's processed or not

bots = [[] for _ in range(BOT_NUM)]
outputs = [[] for _ in range(OUTPUT_NUM)]
compareDetect = [17, 61]

for i in initialGivens:
    bots[i[1]].append(i[0])

while not all(i[-1] for i in instructions):
    for i in instructions:
        bot = bots[i[0]]
        if not i[-1] and len(bot) >= 2:
            if compareDetect[0] in bot and compareDetect[1] in bot:
                print("bro these instructions are actually bad: %i" % i[0])

            secondIndex = 2
            if i[1] == 'output':
                outputs[i[2]].append(min(bot))
                secondIndex = 3
            else:
                bots[i[1]].append(min(bot))

            if i[secondIndex] == 'output':
                outputs[i[secondIndex + 1]].append(max(bot))
            else:
                bots[i[secondIndex]].append(max(bot))
            i[-1] = 1

outputProduct = [0, 1, 2]
prod = 1
for o in outputProduct:
    prod *= outputs[o][0]
print("i mean you'd think the instructions would be in order, but nOOOO: %i" % prod)
