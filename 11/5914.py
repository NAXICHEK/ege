from math import *
a = 26
b = 10
kod1 = ceil(log2(a))
kod2 = ceil(log2(b))
chad = ceil(kod1*26)
chad2 = ceil(kod2*3)
print(ceil((chad+chad2)*38766/1024/8))