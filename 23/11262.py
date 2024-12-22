def f(c, e):
    if c > e or c == 36: return 0
    if c == e: return 1
    return f(c+2, e) + f(c+3, e)
print(f(17, 35)* f(35, 43))