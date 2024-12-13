def cc(x, y):
    s = ''
    while x > 0:
        s = str(x % y) + s
        x = x // y
    return s
a = []
for i in range(1, 100):
    b = cc(i, 3)
    if int(b) % 7 == 0:
        b = b + b[-2] + b[-1]
    else:
        b = b + cc((int(b) % 7) * 3, 3)
    r = int(b, 3)
    a.append(r)
for g in sorted(a):
    if g > 369:
        print(g) # 384
        break
print(sorted(a))