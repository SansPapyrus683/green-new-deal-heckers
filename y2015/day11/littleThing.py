alphabets = list("abcdefghijklmnopqrstuvwxyz")

def testValid(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False

    consecReq = False
    letterPairArchive = []
    for i, c in enumerate(password):
        if i >= 2:  # don't test for first two indexes
            if alphabets.index(password[i-2]) + 1 == alphabets.index(password[i-1]) == alphabets.index(password[i]) - 1:
                consecReq = True

        if i >= 1:
            if password[i-1] == c and i - 1 not in [x[1][1] for x in letterPairArchive]:
                letterPairArchive.append([c, [i-1, i]])

    return consecReq and len(letterPairArchive) >= 2

def incrementPass(password):
    if not password:  # if we need to go up a base (but we don't have too)
        return 'a'
    whatsNext = chr(ord(password[-1]) + 1) if password[-1] != 'z' else 'a'
    if whatsNext == 'a':
        return incrementPass(password[:-1]) + 'a'  # keep recursing deeper until there is no change in base
    else:
        return password[:-1] + whatsNext  # if no carrying, just simple

santaPass = 'vzbxkghb'
while not testValid(santaPass):
    santaPass = incrementPass(santaPass)
print('maybe santa could just choose a newGame password at random: %s' % santaPass)

santaPass = incrementPass(santaPass)
while not testValid(santaPass):
    santaPass = incrementPass(santaPass)

print('but at least now i know his password lol: %s' % santaPass)
