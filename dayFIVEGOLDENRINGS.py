#absolutely meaningless .py file, only for me lol
rings = open('goldenRings.txt')
rings = open('test.txt')
with rings as data:
    for v, s in enumerate(data):
        Data = [int(x) for x in s.split(sep = ',')]
print(Data)
#PART 1 and 2 lol- for part 1, put in 5
waitUntilVal = 0
v = 0
while v <= len(Data):
    i = Data[v]
    if True: #srry ill try getting around to erasing this if clause
        if i in [1,2,3,4,5,6,7,8,99]: #standard protocol
            if i == 3:
                Data[Data[v+1]] = int(input('PUT 1 U DUMB BUTT (unless you want part 2 in which case you put 5)'))
                v += 2
            elif i == 1:
                #print(Data[Data[v+1]], Data[Data[v+2]])
                Data[Data[v + 3]] = Data[Data[v+1]] + Data[Data[v+2]]
                v += 4
            elif i == 2:
                Data[Data[v + 3]] = Data[Data[v+1]] * Data[Data[v+2]]
                v += 4
            elif i == 4:
                print(Data[Data[v+1]])
                #assert Data[Data[v+1]] == 0
                v += 2
            elif i == 5:
                if Data[Data[v+1]] != 0:
                    v = Data[Data[v+2]]
            elif i == 6:
                if Data[Data[v+1]] == 0:
                    v = Data[Data[v+2]]
            elif i == 7:
                Data[Data[v+3]] = 1 if Data[Data[v+1]] < Data[Data[v+2]] else 0
                v += 4
            elif i == 8:
                Data[Data[v+3]] = 1 if Data[Data[v+1]] == Data[Data[v+2]] else 0
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
                            argList.append(Data[v+3])
                        else:
                            argList.append(Data[Data[v+a+1]])
                    else: #if was immediate
                        argList.append(Data[v+a+1])
                #print(argList)
                if saved == 1: #opcode 1
                    Data[argList[2]] = argList[0] + argList[1]
                else: #opcode 2
                    Data[argList[2]] = argList[0] * argList[1]
                v += 4
                #print(i)
            elif saved in [3,4]:
                i = [int(x) for x in list(f'{str(i).zfill(3)}')] #if the opcode was 3 or 4
                if i[-1] == 3:
                    Data[Data[v+1]] = int(input('why does this happen'))
                else:
                    if i[0] == 0:
                        print(Data[Data[v+1]])
                        #assert Data[Data[v+1]] == 0
                    else:
                        print(Data[v+1])
                        #assert Data[v+1] == 0
                v += 2
            elif saved in [5,6]:
                i = [int(x) for x in list(f'{str(i).zfill(4)}')]
                i = i[:-2]; i.reverse
                argList = [] #immediate, positional jump to
                if i[0] == 0: #test
                    argList.append(Data[Data[v+1]])
                else:
                    argList.append(Data[v+1])
                if i[1] == 0: #position the program writes to
                    argList.append(Data[Data[v+2]]) 
                else:
                    argList.append(Data[v+2])
                if saved == 5 and argList[0] != 0:
                    v = argList[1]
                elif argList[0] == 0:
                    v = argList[1]
            elif saved in [7,8]:
                i = [int(x) for x in list(f'{str(i).zfill(5)}')]
                i = i[:3]; i.reverse()
                argList = []
                for a, x in enumerate(i):
                    if x == 0:
                        if a == 2:
                            argList.append(Data[v+3])
                        else:
                            argList.append(Data[Data[v+a+1]])
                    else:
                        argList.append(Data[v+a+1])
                if saved == 7: Data[argList[2]] = 1 if argList[0] < argList[1] else 0
                else: Data[argList[2]] = 1 if argList[0] == argList[1] else 0
                v += 4
#print(Data)