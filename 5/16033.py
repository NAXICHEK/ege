d = []
for i in range(1, 10000):
    b = bin(i)[2:]
    if i % 2 == 0:
        b = b + '01'
    else:
        b = b + '10'
    r = int(b, 2)
    if r > 102:
        d.append(r)
print(sorted(d))