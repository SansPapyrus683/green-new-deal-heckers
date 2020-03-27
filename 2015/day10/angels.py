def lookSay(atFirst):
    consecSeqs = []
    firstTime = True
    buildUp = []
    for c in atFirst:
        if firstTime:
            buildUp.append(c)
            firstTime = False
        else:
            if c == buildUp[-1]:
                buildUp.append(c)
            else:
                consecSeqs.append(buildUp)
                buildUp = [c]
    if buildUp:
        consecSeqs.append(buildUp)

    new = ''
    for seq in consecSeqs:
        new += str(len(seq)) + seq[0]
    return new

telephone = '1113122113'  # string actually makes it easier- you'll see
for i in range(50):
    telephone = lookSay(telephone)
    if i == 39:
        print('HOW BORED ARE THE FRICKIN ELVES: %i' % len(telephone))

print('probs really frickin bored, idk: %i' % len(telephone))
