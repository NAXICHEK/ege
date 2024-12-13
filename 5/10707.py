def f(x):
    s = ''
    while x > 0:
        s = str(x % 6) + s
        x = x // 6
    return s
a = []
for i in range(4, 1000):
    b = f(i)
    if int(b) % 3 == 0:
        b = b + b[0] + b[1]
    else:
        b = b + f((int(b) % 3) * 10)
    r = int(b, 6)
    if r > 680:
        a.append(r)
print(min(a)) # 694