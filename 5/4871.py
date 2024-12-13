c = 0
a = []
for i in range(2, 10000):
    b = i
    if i % 3 == 0:
        b = b / 3
    else:
        b = b - 1
    if b % 5 == 0:
        b = b / 5
    else:
        b = b - 1
    if b % 11 == 0:
        b = b / 11
    else:
        b = b - 1
    if b == 8:
        c += 1

print(c) # 4