"""neptune just reminds me of spongebob
WHO LIVES IN A PINEAPPLE UNDER THE SEA
maybe numpy would be good but heck that"""
placesToGo = [] #itll be a list of tuples
keyLoc = []
assoDoorLoc = []

inFan = open('data stuff/test.txt')
with inFan as stuff:
    yVal = 0
    for l in reversed(stuff.readlines()):
        xVal = 0
        l = l.rstrip()
        for c in list(l):
            if c == '#':
                xVal += 1
            elif c == '.':
                placesToGo.append((xVal, yVal))
            elif c == '@':
                placesToGo.append((xVal, yVal))
                currPos = [xVal, yVal]
            else:
                placesToGo.append((xVal, yVal))
                if c.upper() == c: #door found
                    assoDoorLoc.append((xVal, yVal, c))
                else: #key instead
                    keyLoc.append((xVal, yVal, c))
            xVal += 1
        yVal += 1

print(placesToGo)
print(keyLoc)
print(assoDoorLoc)