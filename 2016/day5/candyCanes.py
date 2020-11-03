from hashlib import md5

start = 'wtnhxymk'
p1code = ''
p2code = ['' for _ in range(8)]
index = 0
while not all(p2code):
    index_hash = md5(f'{start}{index}'.encode('utf-8')).hexdigest()
    if index_hash.startswith("00000"):
        if len(p1code) < 8:
            p1code += index_hash[5]
            if len(p1code) == 8:
                print("ok p1 answer is %s (seriously is there any way to not brute force this)" % p1code)
        if index_hash[5].isdigit() and 0 <= int(index_hash[5]) <= 7 and not p2code[int(index_hash[5])]:
            p2code[int(index_hash[5])] = index_hash[6]
    index += 1

print("second code is %s omg it took so long" % ''.join(p2code))
