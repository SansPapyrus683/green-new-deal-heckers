"""it must suck getting your birthday present as a christmas present"""
from collections import defaultdict

program = []
with open('onePresent.txt') as read:
    for line in read.readlines():
        program.append(line.rstrip().replace(',', '').split())

variables = defaultdict(lambda: 0)
def run(prog, initialVars):  # both part 1 and 2, so..
    index = 0
    while index < len(prog):
        op = prog[index].copy()

        if op[0] == 'inc':
            initialVars[op[1]] += 1
        elif op[0] == 'jio':
            if initialVars[op[1]] == 1:
                index += eval(op[2])
                continue
        elif op[0] == 'jie':
            if not initialVars[op[1]] % 2:
                index += eval(op[2])
                continue
        elif op[0] == 'jmp':
            index += eval(op[1])
            continue
        elif op[0] == 'hlf':
            initialVars[op[1]] /= 2
        elif op[0] == 'tpl':
            initialVars[op[1]] *= 3
        index += 1
    return initialVars

print('this one was ez: %i' % run(program, variables)['b'])
variables = defaultdict(lambda: 0)
variables['a'] = 1
print('though it took me like 15 minutes to realize i misimplemented jio at first: %i' % run(program, variables)['b'])
