from itertools import *

a = "ДЖАВАСКРИПТ"
c = 0
for x in permutations(a):
    slovo = ''.join(x)
    otvet = 0
    for z in range(len(slovo)):
        sovok = slovo[z]
        if (sovok == "А" or sovok == "И"):
            otvet = otvet + (z + 1)
            if (otvet == 11):
                c += 1
                print(slovo)
print(c)