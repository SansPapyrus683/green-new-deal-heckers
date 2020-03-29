from numpy import zeros, nonzero
# shamelessly copied from github, but at least i know how it works
limit = 1000000  # the array of all houses

goal = 33100000
normalHouses = zeros(limit)
tiredHouses = zeros(limit)

for elf in range(1, limit):  # for each elf, calc each houses that it goes to
    normalHouses[elf::elf] += 10 * elf  # go to limit in multiples of the elf's number
    tiredHouses[elf:(elf + 1) * 50:elf] += 11 * elf  # this time, only go up to 50 houses

print('what were the elves doing in the first place anyways: %i' % nonzero(normalHouses >= goal)[0][0])
print("just even more proof that the elves are lazy bums: %i" % nonzero(tiredHouses >= goal)[0][0])
