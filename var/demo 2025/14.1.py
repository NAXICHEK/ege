from string import printable


def f(x):
    s = ''
    d = printable[:25]
    while x > 0:
        s = str(d[x%25]) + s
        x //= 25
    return s
r = f(3 * 3125**8 + 2 * 625**7 - 4*625**6 + 3 * 125**5 - 2 * 25**4 - 2025)
print(r.count('0'))