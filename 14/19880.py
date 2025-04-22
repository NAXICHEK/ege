from string import printable
def f(x):
    s = ''
    d = printable[:25]
    while x > 0:
        s = str(d[x%25]) + s
        x //= 25
    return s
r = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
print(f(r).count('0'))