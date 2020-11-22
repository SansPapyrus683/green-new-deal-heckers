from queue import LifoQueue


def findParenEnd(text: str, start: int):
    parens = LifoQueue()
    parens.put("(")
    parenEnd = start
    while not parens.empty():
        parenEnd += 1
        if text[parenEnd] == "(":
            parens.put("(")
        elif text[parenEnd] == ")":
            parens.get()
    return parenEnd


def p2DecompressLen(toDecomp: str) -> int:
    at = 0
    decompressed_len = 0
    while at < len(toDecomp):
        ch = toDecomp[at]
        if ch == "(":
            pEnd = findParenEnd(toDecomp, at)
            chAfter, repeatN = [int(i) for i in toDecomp[at + 1:pEnd].split("x")]
            # recurse until all the parenthesis are decompressed instead of just moving on
            decompressed_len += p2DecompressLen(toDecomp[pEnd + 1:pEnd + chAfter + 1]) * repeatN
            at = pEnd + chAfter
        else:
            decompressed_len += 1
        at += 1
    return decompressed_len


compressed = open('whatsThePrettiest.txt').read().rstrip()

# why does it ask us to not count whitespace it's not like there's any in the input
char_at = 0
decompressed = ""
while char_at < len(compressed):
    c = compressed[char_at]
    if c == "(":
        end = findParenEnd(compressed, char_at)
        charsAfter, repeatNum = [int(i) for i in compressed[char_at + 1:end].split("x")]
        decompressed += compressed[end + 1:end + charsAfter + 1] * repeatNum
        char_at = end + charsAfter
    else:
        decompressed += c
    char_at += 1

print("why is this file so interesting lol: %s" % len(decompressed))
print("bruh the protagonist JUST realized it was version two? %s" % p2DecompressLen(compressed))
