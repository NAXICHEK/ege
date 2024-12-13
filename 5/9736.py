f = []
for i in range(10000):
    a = str(bin(i)[2:])
    if i % 3 == 0:
        a = a + a[-3:]
    else:
        a = a + str(bin((i % 3) * 3))[2:]
    r = int(a, 2)
    f.append(r)
    if r > 1400:
        print(r)
        break
# f.sort()
# print(*f)
# #1661