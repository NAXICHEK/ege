a = []
for n in range(1000):
    b = n
    n = bin(n)[2:]
    if b % 3 == 0:
        n = '1' + n[:-2] + '11'
    else:
        n = '10' + n + '0'
    if b % 2 == 0:
        a.append(int(n, 2))
        if int(n, 2) > 999:
            print(int(n, 2))

a.sort()
print(*a)