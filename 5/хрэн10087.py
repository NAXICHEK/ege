a = []
for i in range(1, 100):
    b = bin(i)[2:]
    if int(b) % 3 == 0:
        b = b + b[-3] + b[-2] + b[-1]
    else:
        b = b + bin((int(b) % 3) * 3)[2:]
    r = int(b, 2)
    a.append(r)
for g in sorted(a):
    if g > 151:
        print(g)