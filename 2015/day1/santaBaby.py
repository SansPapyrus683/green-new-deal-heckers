floor = 0
basementTime = False
directions = open('riceRolex.txt').read().rstrip()
for v, c in enumerate(directions):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor < 0 and not basementTime:
        print('well he enters the basement at this position: %i (part 2 ans)' % (v + 1))
        basementTime = True
# i kno part 2 before part 1 is kinda awkward but frick it, idc
print(floor, "No apartment building in the WORLD is this tall... (part 1 ans)")
