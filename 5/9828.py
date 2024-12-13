def f(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x // 3
    return s

a = []

for i in range(1, 1000):
    b = f(i)
    if i % 3 == 0:
        b = '1' + b + '02'
    else:
        b = b + f((i % 3) * 4)
    r = int(b, 3)
    if r < 199:
        a.append(i)
print(max(a))