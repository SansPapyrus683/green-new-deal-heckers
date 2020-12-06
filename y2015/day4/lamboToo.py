from hashlib import md5

secKey = 'yzbqklnj'
i = 0
fiveZSearch = True
while True:
    result = md5((secKey + str(i)).encode())
    if result.hexdigest()[:5] == '00000' and fiveZSearch:
        print(i, 'santa what are you doing with your life')  # part 1
        fiveZSearch = False
    elif result.hexdigest()[:6] == '000000':
        print(i, 'capitalism boiiis')  # part 2
        break
    i += 1
 # don't check backwards because we already checked it
 