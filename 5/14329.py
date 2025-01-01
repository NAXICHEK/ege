def f(x):
    s = ''
    while x > 0:
        s = str(x % 4) + s
        x //= 4
    return s
a = []
for i in range(1, 1000):
    b = f(i)
    if i % 4 == 0:
        b = b + b[:2]
    else:
        b = b + f((i%4)*4)
    r = int(b, 4)
    if r > 291:
        a.append(r)
print(min(a))