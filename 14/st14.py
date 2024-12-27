def f(x):
    s = ''
    while x > 0:
        s = str(x%7) + s
        x //= 7
    return s

for x in range(100000000000):
    r = f(4*7**24 + 6*7**13 + 5*49**4 + 2*343**2 + 10 - x)
    if str(r).count('6') > str(r).count('0'):
        print(x)