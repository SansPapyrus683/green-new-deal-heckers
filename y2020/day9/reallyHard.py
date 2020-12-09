previousNum = 25

with open('toSleepTonight.txt') as read:
    numbers = [int(i) for i in read.readlines()]

invalidNum = -1
for i in range(previousNum, len(numbers)):
    allPrev = numbers[i - previousNum:i]
    valid = False
    for j in range(previousNum):
        for k in range(previousNum):
            if j != k and allPrev[j] + allPrev[k] == numbers[i]:
                valid = True
                break
        if valid:
            break
    if not valid:
        invalidNum = numbers[i]
        print("ok what are we even trying to do here: %i" % invalidNum)
        break

if invalidNum == -1:
    raise ValueError("hold on here i thought there was always going to be an invalid number")

prefixSum = [0]  # this speeds it up SO much faster lol
for n in numbers:
    prefixSum.append(prefixSum[-1] + n)
# i think with a sliding windows like in https://www.geeksforgeeks.org/find-subarray-with-given-sum/ you can get faster
# but with 1000 lines it doesn't really matter
for i in range(len(numbers)):
    for j in range(i + 2, len(numbers)):  # the subset has to contain at least 2 numbers
        subSum = prefixSum[j + 1] - prefixSum[i]
        if subSum == invalidNum:
            subset = numbers[i:j]
            print("i thought planes were supposed to have like user-friendly UIs: %i" % (min(subset) + max(subset)))
