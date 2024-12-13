f = []
m = 1111111111111111111000000000000
for n in range(1, 1000):
    b = bin(n)[2:]
    if len(b) % 2 == 0:
        b = b + '1'
    else:
        b = '1' + b + '0'
    r = int(b, 2)
    f.append(r)
    if r > 666:
        m = min(m, r)
        print(m) # 1025
print(sorted(f))