lightGrid = {(x, y): False for x in range(1000) for y in range(1000)}
brightnessGrid = lightGrid.copy()  # don't worry, False is pretty much the same as 0

def onOffOp(xRange, yRange, operation):  # unlike python ranges, these ranges are inclusive
    global lightGrid
    for x in range(xRange[0], xRange[1] + 1):
        for y in range(yRange[0], yRange[1] + 1):
            lightGrid[(x, y)] = operation(lightGrid[(x, y)])

def brightnessOp(xRange, yRange, operation):
    global brightnessGrid
    for x in range(xRange[0], xRange[1] + 1):
        for y in range(yRange[0], yRange[1] + 1):
            brightnessGrid[(x, y)] = operation(brightnessGrid[(x, y)])

def turnOff(currB):
    if currB == 0:
        return 0
    return currB - 1

with open('santaBetterHurry.txt') as read:
    for instruction in read.readlines():
        instruction = instruction.replace(' through ', ',')
        if instruction[6] == 'n':  # turn on all lights in this range
            instruction = [int(i) for i in instruction[8:].split(sep=',')]
            instruction = [sorted([instruction[0], instruction[2]]), sorted([instruction[1], instruction[3]])]
            onOffOp(instruction[0], instruction[1], lambda b: True)
            brightnessOp(instruction[0], instruction[1], lambda b: b + 1)
        elif instruction[1] == 'o':  # toggle
            instruction = [int(i) for i in instruction[7:].split(sep=',')]
            instruction = [sorted([instruction[0], instruction[2]]), sorted([instruction[1], instruction[3]])]
            onOffOp(instruction[0], instruction[1], lambda b: not b)
            brightnessOp(instruction[0], instruction[1], lambda b: b + 2)
        else:  # turn off all these lights
            instruction = [int(i) for i in instruction[9:].split(sep=',')]
            instruction = [sorted([instruction[0], instruction[2]]), sorted([instruction[1], instruction[3]])]
            onOffOp(instruction[0], instruction[1], lambda b: False)
            brightnessOp(instruction[0], instruction[1], turnOff)

onCount = 0
for light in lightGrid.values():
    if light:
        onCount += 1

print(onCount, "what's your electric bill going to be after this anyways")
print(sum(brightnessGrid.values()), "probs going to be pretty darn high - it's a MILLION fricking lights!")
