def validField(field, value):
    if field == 'byr':
        return value.isdigit() and 1920 <= int(value) <= 2002
    elif field == 'iyr':
        return value.isdigit() and 2010 <= int(value) <= 2020
    elif field == 'eyr':
        return value.isdigit() and 2020 <= int(value) <= 2030
    elif field == 'hgt':
        height = value[:-2]
        if value[-2:] == 'in':
            return height.isdigit() and 59 <= int(height) <= 76
        elif value[-2:] == 'cm':
            return height.isdigit() and 150 <= int(height) <= 193
    elif field == 'hcl':
        return value[0] == '#' and len(value) == 7 and all(v.isdigit or v.isalpha() for v in value[1:])
    elif field == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif field == 'pid':
        return len(value) == 9 and value.isdigit()
    return False


passports = []
with open('waitReallyTho.txt') as read:
    currString = ""
    for line in read.readlines():
        line = line.rstrip()
        if not line:
            passports.append(currString.strip().split())
            currString = ""
        else:
            currString += line + " "
    passports.append(currString.strip().split())  # there's still a string left in input, let's append that

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
p1Valid = 0
p2Valid = 0
for p in passports:
    fields = {f[:f.find(':')] for f in p}
    if required.issubset(fields):
        p1Valid += 1
        for f in p:
            name = f[:f.find(':')]
            if name in required and not validField(name, f[f.find(':') + 1:]):
                break
        else:
            p2Valid += 1

print("this one seriously reminds me of papers please: %i" % p1Valid)
print("glory to advent of code. %i" % p2Valid)
