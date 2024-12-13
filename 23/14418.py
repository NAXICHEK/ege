def f(c, e, d):
    if c > e: return 0
    if c == e: return 1
    return f(c+d, e, d) + f(c*2, e, d)

for i in range(1, 100):
    if f(1, 10, i)*f(10, 100, i) == 13:
        print(i)