def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c+3, e) + f(c+2, e)
print(f(8, 28)*f(28,31)*f(31, 43))