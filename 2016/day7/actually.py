import re


def abbaPrescence(s: str) -> bool:
    for i in range(3, len(s)):
        if s[i - 3] == s[i] and s[i - 2] == s[i - 1] and s[i - 1] != s[i]:
            return True
    return False


def abaAndBAB(out: [str], inside: [str]):
    for o in out:
        for i in range(2, len(o)):
            if o[i] == o[i - 2] and o[i] != o[i - 1]:
                for ins in inside:
                    if f"{o[i - 1]}{o[i]}{o[i - 1]}" in ins:
                        return True
    return False


addresses = []
with open('looksLikeChristmas.txt') as read:
    for l in read.readlines():
        addresses.append(l.rstrip())

tlsValid = 0
sslValid = 0
for v, a in enumerate(addresses):
    supportsTLS = False

    outBrackets = re.split(r"\[[a-z]*]", a)
    inBrackets = re.findall(r"\[([^]]+)]", a)
    for seg in outBrackets:  # i mean only alphabet anyways
        if abbaPrescence(seg):
            for brackSeg in inBrackets:
                if abbaPrescence(brackSeg):
                    supportsTLS = False
                    break
            else:
                supportsTLS = True
            break

    tlsValid += 1 if supportsTLS else 0
    sslValid += 1 if abaAndBAB(outBrackets, inBrackets) else 0

print("iirc ipv7 also had number or im just dumb: %s" % tlsValid)
print("also where did the protagonist get the ip addresses: %s" % sslValid)
