from itertools import permutations
data = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,6,27,1,27,5,31,2,6,31,35,1,5,35,39,2,39,9,43,1,43,5,47,1,10,47,51,1,51,6,55,1,55,10,59,1,59,6,63,2,13,63,67,1,9,67,71,2,6,71,75,1,5,75,79,1,9,79,83,2,6,83,87,1,5,87,91,2,6,91,95,2,95,9,99,1,99,6,103,1,103,13,107,2,13,107,111,2,111,10,115,1,115,6,119,1,6,119,123,2,6,123,127,1,127,5,131,2,131,6,135,1,135,2,139,1,139,9,0,99,2,14,0,0]
data[1], data[2] = 12, 2
values = [[a,b] for (a,b) in permutations(list(range(0,100)), 2)]
#first part
for v, i in enumerate(data):
    if v%4 == 0:
        if i == 1:
            data[data[v + 3]] = data[data[v+1]] + data[data[v+2]]
        elif i == 2:
            data[data[v + 3]] = data[data[v+1]] * data[data[v+2]]
        elif i == 99:
            print(data[0])
            break

#seond part (i had to refresh the data)
data = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,6,27,1,27,5,31,2,6,31,35,1,5,35,39,2,39,9,43,1,43,5,47,1,10,47,51,1,51,6,55,1,55,10,59,1,59,6,63,2,13,63,67,1,9,67,71,2,6,71,75,1,5,75,79,1,9,79,83,2,6,83,87,1,5,87,91,2,6,91,95,2,95,9,99,1,99,6,103,1,103,13,107,2,13,107,111,2,111,10,115,1,115,6,119,1,6,119,123,2,6,123,127,1,127,5,131,2,131,6,135,1,135,2,139,1,139,9,0,99,2,14,0,0]
for testee in values:
	newData = data[:]
	newData[1], newData[2] = testee[0], testee[1]
	for v, i in enumerate(newData):
		if v%4 == 0:
			if i == 1:
				newData[newData[v + 3]] = newData[newData[v+1]] + newData[newData[v+2]]
			elif i == 2:
				newData[newData[v + 3]] = newData[newData[v+1]] * newData[newData[v+2]]
			elif i == 99:
				if newData[0] == 19690720:
					print(testee)