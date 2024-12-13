def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c+3, e) + f(c+4, e) + f(c+2, e)
print(f(6, 32)*f(32, 35)*f(35, 44)) # 82808