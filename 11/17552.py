# import math as m
# for kod in range(1,1000):
#     c = m.ceil(m.log2(kod))
#     parol = m.ceil(261*c/8)
#     if 252500*parol > 31*2**20:
#         print(kod)
#         break

from math import *
for i in range(1,1000):
    a = ceil(log2(i))
    chad = ceil(261 * a/8)
    if chad * 252500 > 31*1024*1024:
        print(i)
        break