"""
ok so i guess ill have to explain this one cuz its so long
so the way i did this is that i put two conditionals- 
one for normal and another for immediate and positional args
then for each i split them into their respective "genres", as
you will see in the program
"""
rings = open('goldenRings.txt')
rings = open('test.txt')
with rings as data:
    for v, s in enumerate(data):
        Data = [int(x) for x in s.split(sep = ',')]
#PART 1 and 2 lol- for part 1, put in a 1 but for part 2 put in a 5
from justStupidIntcode import intCode
intcode = intCode(Data)
intcode.interpret()