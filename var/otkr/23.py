def f(c, e):
    if c > e or c == 8: return 0
    if c == e: return 1
    return f(c+1, e) + f(c+2, e) + f(c*2, e)

print(f(3, 14) * f(14, 18))