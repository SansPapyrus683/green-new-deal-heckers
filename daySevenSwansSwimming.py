from itertools import permutations
with open('swanLake.txt') as data:
    for line in data.readlines():
        Data = [int(x) for x in line.rstrip().split(sep = ',')]
#print(Data)
#PART 1
possibilites = permutations([0,1,2,3,4])
#the following intcode run is only for this day that has manual input
def intCodeRunPtOne(settings, code):
    output = 0
    for o in range(5):
        v = 0
        count = 0
        while v <= len(code):
            i = code[v]
            if i in [1,2,3,4,5,6,7,8,99]: #standard protocol
                if i == 3:
                    #code[code[v+1]] = int(input('input settings or smth')) <- this wont be necessary
                    count += 1
                    if count == 2: code[code[v+1]] = output
                    else: code[code[v+1]] = settings[o]
                    v += 2
                elif i == 1:
                    #print(code[code[v+1]], code[code[v+2]])
                    code[code[v + 3]] = code[code[v+1]] + code[code[v+2]]
                    v += 4
                elif i == 2:
                    code[code[v + 3]] = code[code[v+1]] * code[code[v+2]]
                    v += 4
                elif i == 4:
                    output = code[code[v+1]]
                    break
                    #print(code[code[v+1]])
                    v += 2
                elif i == 5:
                    if code[code[v+1]] != 0:
                        v = code[code[v+2]]
                elif i == 6:
                    if code[code[v+1]] == 0:
                        v = code[code[v+2]]
                elif i == 7:
                    code[code[v+3]] = 1 if code[code[v+1]] < code[code[v+2]] else 0
                    v += 4
                elif i == 8:
                    code[code[v+3]] = 1 if code[code[v+1]] == code[code[v+2]] else 0
                    v += 4
                elif i == 99:
                    break
            elif str(i)[-2:] in ['01', '02', '03', '04','05','06','07','08', '99']: #0 is position, 1 is immediate
                saved = int(str(i)[-1])
                if saved == 99:
                    break
                elif saved in [1,2]:
                    i = [int(x) for x in list(f'{str(i).zfill(5)}')]
                    i = i[:3]; i.reverse()
                    #print(i)
                    argList = [] #immediate, immediate, positional
                    for a, x in enumerate(i):
                        if x == 0: #if the one taken is a positional
                            if a == 2:
                                argList.append(code[v+3])
                            else:
                                argList.append(code[code[v+a+1]])
                        else: #if was immediate
                            argList.append(code[v+a+1])
                    #print(argList)
                    if saved == 1: #opcode 1
                        code[argList[2]] = argList[0] + argList[1]
                    else: #opcode 2
                        code[argList[2]] = argList[0] * argList[1]
                    v += 4
                    #print(i)
                elif saved in [5,6]:
                    i = [int(x) for x in list(f'{str(i).zfill(4)}')]
                    i = i[:-2]; i.reverse()
                    argList = [] #immediate, positional jump to
                    if i[0] == 0: #test
                        argList.append(code[code[v+1]])
                    else:
                        argList.append(code[v+1])
                    if i[1] == 0: #position the program writes to
                        argList.append(code[code[v+2]]) 
                    else:
                        argList.append(code[v+2])
                    if saved == 5 and argList[0] != 0:
                        v = argList[1]
                        continue
                    elif saved == 6 and argList[0] == 0:
                        v = argList[1]
                        continue
                    v += 3
                elif saved in [7,8]:
                    i = [int(x) for x in list(f'{str(i).zfill(5)}')]
                    i = i[:3]; i.reverse()
                    argList = []
                    for a, x in enumerate(i):
                        if x == 0:
                            if a == 2:
                                argList.append(code[v+3])
                            else:
                                argList.append(code[code[v+a+1]])
                        else:
                            argList.append(code[v+a+1])
                    if saved == 7: code[argList[2]] = 1 if argList[0] < argList[1] else 0
                    else: code[argList[2]] = 1 if argList[0] == argList[1] else 0
                    v += 4
    return output

outputs = []
for v, p in enumerate(possibilites):
    outputs.append(intCodeRunPtOne(p, Data))
#print(max(outputs))

#PART 2
from stupidIntcode import intCode
possibilites = permutations([5,6,7,8,9])
def intCodeRunPtTwo(settings, code):
    copy = code[:]
    output = 0
    while True:
        for o in range(5):
            #print('here',o, output)
            v = 0
            count = 0
            code = copy[:]
            while v <= len(code):
                #print(v, code[v])
                i = code[v]
                if i in [1,2,3,4,5,6,7,8,99]: #standard protocol
                    if i == 3:
                        count += 1
                        if count == 2: code[code[v+1]] = output
                        elif count == 1: code[code[v+1]] = settings[o]
                        #print(settings[o], o)
                        v += 2
                    elif i == 1:
                        #print(code[code[v+1]], code[code[v+2]])
                        code[code[v + 3]] = code[code[v+1]] + code[code[v+2]]
                        v += 4
                    elif i == 2:
                        code[code[v + 3]] = code[code[v+1]] * code[code[v+2]]
                        v += 4
                    elif i == 4:
                        output = code[code[v+1]]
                        #print(code[code[v+1]])
                        v += 2
                    elif i == 5:
                        if code[code[v+1]] != 0:
                            v = code[code[v+2]]
                    elif i == 6:
                        if code[code[v+1]] == 0:
                            v = code[code[v+2]]
                    elif i == 7:
                        code[code[v+3]] = 1 if code[code[v+1]] < code[code[v+2]] else 0
                        v += 4
                    elif i == 8:
                        code[code[v+3]] = 1 if code[code[v+1]] == code[code[v+2]] else 0
                        v += 4
                    elif i == 99 and o == 4:
                        return output
                    elif i == 99:
                        break
                elif str(i)[-2:] in ['01', '02', '03', '04','05','06','07','08', '99']: #0 is position, 1 is immediate
                    saved = int(str(i)[-1])
                    if saved == 99 and o == 4:
                        return output
                    elif saved == 99:
                        break
                    elif saved in [1,2]:
                        i = [int(x) for x in list(f'{str(i).zfill(5)}')]
                        i = i[:3]; i.reverse()
                        #print(i)
                        argList = [] #immediate, immediate, positional
                        for a, x in enumerate(i):
                            if x == 0: #if the one taken is a positional
                                if a == 2:
                                    argList.append(code[v+3])
                                else:
                                    argList.append(code[code[v+a+1]])
                            else: #if was immediate
                                argList.append(code[v+a+1])
                        #print(argList)
                        if saved == 1: #opcode 1
                            code[argList[2]] = argList[0] + argList[1]
                        else: #opcode 2
                            code[argList[2]] = argList[0] * argList[1]
                        v += 4
                        #print(i)
                    elif saved in [5,6]:
                        i = [int(x) for x in list(f'{str(i).zfill(4)}')]
                        i = i[:-2]; i.reverse()
                        argList = [] #immediate, positional jump to
                        if i[0] == 0: #test
                            argList.append(code[code[v+1]])
                        else:
                            argList.append(code[v+1])
                        if i[1] == 0: #position the program writes to
                            argList.append(code[code[v+2]]) 
                        else:
                            argList.append(code[v+2])
                        if saved == 5 and argList[0] != 0:
                            v = argList[1]
                            continue
                        elif saved == 6 and argList[0] == 0:
                            v = argList[1]
                            continue
                        v += 3
                    elif saved in [7,8]:
                        i = [int(x) for x in list(f'{str(i).zfill(5)}')]
                        i = i[:3]; i.reverse()
                        argList = []
                        for a, x in enumerate(i):
                            if x == 0:
                                if a == 2:
                                    argList.append(code[v+3])
                                else:
                                    argList.append(code[code[v+a+1]])
                            else:
                                argList.append(code[v+a+1])
                        if saved == 7: code[argList[2]] = 1 if argList[0] < argList[1] else 0
                        else: code[argList[2]] = 1 if argList[0] == argList[1] else 0
                        v += 4
    return output
outputs = []
assoscitasdf = []
"""
for v, p in enumerate(possibilites):
    outputs.append([intCodeRunPtTwo(p, Data), v])
    assoscitasdf.append(p)
print(max(outputs))
"""
print(intCodeRunPtTwo([9,8,7,6,5], Data))