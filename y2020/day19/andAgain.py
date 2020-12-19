def matches(msg, rules, ruleNum=0):
    rule = rules[ruleNum]
    if type(rule) == str:
        if msg.startswith(rule):
            return [msg[len(rule):]]
        return []
    elif type(rule) == list:
        valid = []
        for subruleSeq in rule:
            remains = [msg]
            for subr in subruleSeq:
                leftovers = []
                for r in remains:
                    leftovers.extend(matches(r, rules, subr))
                remains = leftovers
            valid.extend(remains)
        return valid
    else:
        raise ValueError("your rules don't follow my rules lol")


daRules = {}
messages = []
with open('everyMomsKid.txt') as read:
    parsingRules = True
    for line in read.readlines():
        line = line.strip()
        if not line:
            parsingRules = False
            continue
        elif parsingRules:
            line = line.split(':')
            ruleNum = int(line[0])
            daRules[ruleNum] = []
            rule = line[1]
            if any(c.isalpha() for c in rule):
                daRules[ruleNum] = rule[rule.find('"') + 1:rule.rfind('"')]
            else:
                for subrule in rule.split('|'):
                    daRules[ruleNum].append([int(i) for i in subrule.split()])
        else:
            messages.append(line)

allMatching = [m for m in messages if '' in matches(m, daRules, 0)]
print("what kind of message only has a's and b's: %i" % len(allMatching))
daRules[8] = [[42], [42, 8]]
daRules[11] = [[42, 31], [42, 11, 31]]
allMatching = [m for m in messages if '' in matches(m, daRules, 0)]
print("seems kinda... limited, but who am i to judge: %i" % len(allMatching))
