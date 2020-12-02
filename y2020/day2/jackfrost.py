with open('nippingOnNose.txt') as read:
    passwords = [p.rstrip() for p in read.readlines()]

p1Valid = 0
p2Valid = 0
for p in passwords:
    numbers, char = p[:p.find(':')].split()
    num1 = int(numbers[:numbers.find('-')])
    num2 = int(numbers[numbers.find('-') + 1:])
    passw = p[p.find(':') + 1:].strip()
    if num1 <= passw.count(char) <= num2:
        p1Valid += 1
    if (passw[num1 - 1] == char) ^ (passw[num2 - 1] == char):
        p2Valid += 1

print("i absolutely hate input provided like this: %i" % p1Valid)
print("but i guess i can't do anything about it: %i" % p2Valid)
