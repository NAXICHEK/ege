def cc(x):
    s = ''
    while x > 0:
        s = str(x%5) + s
        x //= 5
    return s
m = 0
for i in range(2006):
    r = 4**163 * 5 + 12**62 - i
    a = cc(r)

    if a.count('1') < a.count('4'):
        m = max(m, i)
print(m)