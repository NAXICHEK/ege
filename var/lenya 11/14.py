from string import printable


def f(x):
    s = ''
    d = printable[:17]
    while x > 0:
        s = d[x%17] + s
        x //= 17
    return s
s = f(3 * 17**777 + 15*17**250 - 6*17**100 + 2)
d = set()
for i in s:
    if int(i, 17) % 2 == 0:
        d.add(i)
print(len(d))