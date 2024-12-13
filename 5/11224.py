def f(x, y):
    s = ''
    while x > 0:
        s = str(x%y) + s
        x = x // y
    return s
a = []
for i in range(1, 1000):
    b = f(i, 3)
    if sum(map(int, b)) % 4 == 0:
        b = '1' + b[:-2]
    else:
        b = b + f((sum(map(int, b)) % 4)*3, 3)
    r = int(b, 3)
    a.append(r)
print(sorted(a))