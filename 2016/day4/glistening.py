from string import ascii_lowercase
from functools import cmp_to_key
from collections import Counter

codes = []
with open('onceAgain.txt') as read:
    for l in read.readlines():
        codes.append(l.rstrip())


def processCode(raw: str) -> (str,):
    checksum = raw[raw.find('[') + 1:-1]
    letters = ''.join([ch for ch in raw[:raw.find('[')] if ch.isalpha()])
    return letters, checksum


def valid(letters: str, checksum: str) -> bool:
    def cmp(a, b):
        return a[1] - b[1] if a[1] != b[1] else ord(b[0]) - ord(a[0])

    assert letters.isalpha and checksum.isalpha()
    mostCommon = sorted(Counter(letters).most_common(), key=cmp_to_key(cmp), reverse=True)
    return ''.join([o[0] for o in mostCommon[:len(checksum)]]) == checksum


def decrypt(code: str) -> str:
    sector = int(c[c.rfind('-') + 1:c.find('[')])
    decoded = ''
    for ch in [ch for ch in code[:code.find('[')] if ch.isalpha()]:
        decoded += ascii_lowercase[(ord(ch) - ord('a') + sector) % 26]
    return decoded


sectorSum = 0
for c in codes:
    if valid(*processCode(c)):
        sectorID = int(c[c.rfind('-') + 1:c.find('[')]);
        sectorSum += sectorID
        print(decrypt(c), sectorID)
print(f"why not just have us find the amt of valid things i mean (part 1): {sectorSum}")
