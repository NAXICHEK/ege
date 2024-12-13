def f(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x // 3
    return s

a = []

for i in range(1, 130000):
    b = f(i)
    if i % 3 == 0:
        b = b + b[:2]
    else:
        b = b + f((int(b) % 3) * 5)
    r = int(b, 3)
    if r > 64:
        a.append(r)
print(min(a)) # 68