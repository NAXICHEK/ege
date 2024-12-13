c = 0
def f(c, e, d):
    if c > e or c == 30: return 0
    if c == e: return 1
    return f(c+d, e, d) + f(c*2, e, d)
print(sum(f(1, 10, i) * f(10, 100, i) for i in range(1, 100000)))