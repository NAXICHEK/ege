def f(x):
    s = ''
    d = '0123456789abcdefghijklmnopqrstuvwxyz'
    while x > 0:
        s = d[x%7] + s
        x //= 7
    return s
for i in range(2031):
    s = f(7**170 + 7**100 - i)
    if s.count('0') == 71:
        print(i) # 2029