rings = open('goldenRings.txt')
#rings = open('test.txt')
with rings as data:
    for v, s in enumerate(data):
        Data = [int(x) for x in s.split(sep = ',')]
print(Data)
#PART 1
waitUntilVal = 0
for v, i in enumerate(Data):
    if v >= waitUntilVal:
        if i in [1,2,3,4,99]: #standard protocol
            if i == 3:
                Data[Data[v+1]] = int(input('PUT 1 U DUMB BUTT '))
                waitUntilVal += 2
            elif i == 1:
                #print(Data[Data[v+1]], Data[Data[v+2]])
                Data[Data[v + 3]] = Data[Data[v+1]] + Data[Data[v+2]]
                waitUntilVal += 4
            elif i == 2:
                Data[Data[v + 3]] = Data[Data[v+1]] * Data[Data[v+2]]
                waitUntilVal += 4
            elif i == 4:
                print(Data[Data[v+1]])
                assert Data[Data[v+1]] == 0
                waitUntilVal += 2
        elif str(i)[-2:] in ['01', '02', '03', '04', '99']: #0 is position, 1 is immediate
            saved = str(i)[-2:]
            if str(i)[-2:] == '99':
                break
            elif str(i)[-2:] in ['01', '02']:
                i = [int(x) for x in list(f'{i:05}')]
                i = i[:3]; i.reverse()
                #print(i)
                argList = [] #immediate, immediate, positional
                for a, x in enumerate(i):
                    if x == 0: #if the one taken is a positional
                        if a == 2:
                            argList.append(Data[v+3])
                        else:
                            argList.append(Data[Data[v+a+1]])
                    else: #if was immediate
                        argList.append(Data[v+a+1])
                #print(argList)
                if saved == '01':
                    Data[argList[2]] = argList[0] + argList[1]
                else:
                    Data[argList[2]] = argList[0] * argList[1]
                #print(i)
            else:
                i = [int(x) for x in list(f'{i:3}')] #if the opcode was 3 or 4
                if i[-1] == 3:
                    Data[Data[v+1]] = int(input('why does this happen'))
                else:
                    if i[0] == 0:
                        print(Data[Data[v+1]])
                        assert Data[Data[v+1]] == 0
                    else:
                        print(Data[v+1])
                        assert Data[v+1] == 0
    print(Data[:v+1], len(Data[:v+1]))
#print(Data)