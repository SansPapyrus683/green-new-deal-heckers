with open('pears.txt') as data:
    newData = [int(i) for i in data.read().split(sep="\n")]

# part 1
fuelCount = 0
for i in newData:
    fuelCount += i // 3 - 2
print('fuel count is go- %i' % fuelCount)


# part 2
def fuelCeption(fuelAmt):  # this calculates the fuel all the way from the mass
    adoptedFuelCount = 0
    while fuelAmt // 3 - 2 > 0:
        adoptedFuelCount += fuelAmt // 3 - 2
        fuelAmt = fuelAmt // 3 - 2
    return adoptedFuelCount


returnOfTheFuelCount = 0
for i in newData:
    returnOfTheFuelCount += fuelCeption(i)
print('i feel apollo flashbacks- %i' % returnOfTheFuelCount)
