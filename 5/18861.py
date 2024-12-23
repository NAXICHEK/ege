def f(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s

for i in range(1, 10000):
    b = f(i)
    if b[-2:] == '10': b = '2' + b
    else: '1' + b
    r = int(b, 3)
    if r > 130:
        print(i)
        break