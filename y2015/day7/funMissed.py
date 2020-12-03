from copy import deepcopy

circuit = {}
actualVals = {}
asdf = []
with open('kissyKiss.txt') as read:
    for c in read.readlines():
        asdf.append(c.rstrip())
        c = c.rstrip().replace(' -> ', ' ')
        if 'LSHIFT' in c:
            c = c.replace(' LSHIFT ', ' ').split()
            circuit[c[2]] = [c[0], '<<', c[1]]
        elif 'RSHIFT' in c:
            c = c.replace(' RSHIFT ', ' ').split()
            circuit[c[2]] = [c[0], '>>', c[1]]
        elif 'AND' in c:
            c = c.replace(' AND ', ' ').split()
            circuit[c[2]] = [c[0], '&', c[1]]
        elif 'NOT' in c:
            c = c.replace('NOT ', ' ').split()
            circuit[c[1]] = ['~', c[0]]
        elif 'OR' in c:
            c = c.replace(' OR ', ' ').split()
            circuit[c[2]] = [c[0], '|', c[1]]
        else:
            if c.split()[0].isalpha():  # unless it's directly another circuit, in which case add it
                circuit[c.split()[1]] = [c.split()[0]]
            else:
                actualVals[c.split()[1]] = c.split()[0]  # put it in the places that've already evaluated

def run(providedCircuit):
    thisVals = deepcopy(actualVals)
    newCircuit = deepcopy(providedCircuit)
    while newCircuit:
        for g in newCircuit.items():
            validOne = True
            for o in g[1]:
                if o.isalpha() and o not in thisVals:
                    validOne = False
                    break
            if validOne:
                break

        if validOne:
            operation = g[1]
            for v, o in enumerate(operation):
                if o.isalpha():
                    operation[v] = thisVals[o]
            if operation[0] == '~':  # the bitwise NOT has to be manually implemented oof
                thisVals[g[0]] = str(65535 - int(operation[1]))
            else:
                thisVals[g[0]] = str(eval(''.join(operation)))
            del newCircuit[g[0]]
    return thisVals

# PART 1
print('well, the signal for circuit a is %s, but WHAT KIND OF GIFT IS BOBBY\'S???' % run(circuit)['a'])

# PART 2
otherCircuit = circuit.copy()
if 'b' in actualVals:
    actualVals['b'] = run(circuit)['a']
else:
    otherCircuit['b'] = run(circuit)['a']

print('and what is bobby\'s age anyways? %s' % run(otherCircuit)['a'])
