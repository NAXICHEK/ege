def f(x):
    s = ''
    while x > 0:
        s = str(x%8) + s
        x //= 8
    return s

a = []

for i in range(1, 10000):
    b = f(i)
    if (b.count('2') + b.count('4') + b.count('6') + b.count('0')) % 2 != 0:
        b = b[-3:] + '46'
    else:
        b = f((i%8)*5) + b
    r = int(b, 8)
    if i >= 90:
        a.append(r)
print(min(a))