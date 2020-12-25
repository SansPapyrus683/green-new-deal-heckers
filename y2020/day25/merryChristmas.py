# yes i know the file name is exactly the same but i mean the song does repeat the lyrics so...

MOD = 20201227
MUL_BY = 7

card = 11562782
door = 18108497

cardLoop = 1
soFar = 1
while True:
    soFar = (soFar * MUL_BY) % MOD
    if soFar == card:
        break
    cardLoop += 1

print("good god i hate this day with the burning passion of a million suns: %i" % pow(door, cardLoop, MOD))
