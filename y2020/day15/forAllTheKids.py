from typing import List

said = [2, 15, 0, 9, 1, 20]


def allSaidNumbers(numbers: List[int], simUntil: int):
    numbers = numbers.copy()
    recent = {}
    for v, n in enumerate(numbers[:-1]):  # don't process the last element just yet
        recent[n] = v

    for _ in range(simUntil - len(numbers)):  # just brute force simulate
        previous = numbers[-1]
        if previous not in recent:
            numbers.append(0)
        else:
            # no idea why the -1 is necessary, think it's because of that 0-indexing
            numbers.append(len(numbers) - 1 - recent[previous])
        # -2 because we already appended the thing, so we have to go back 1 more
        recent[numbers[-2]] = len(numbers) - 1 - 1
    return numbers


print("this is the most boring game of All Time: %i" % allSaidNumbers(said, 2020)[-1])
print("who has patience to recite till the THIRTY MILLIONTH NUM: %i" % allSaidNumbers(said, 30000000)[-1])
