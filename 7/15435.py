from math import *
a = 1920*1080 * log2(2048)
print(ceil(((a + (5 * 1024 * 8))*3*60*24)/1024/1024/8)) # 11768