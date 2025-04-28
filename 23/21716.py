def f(c, e):
    if c > e or c == 56: return 0
    if c == e: return 1
    return f(c+3, e) + f(c+7, e) + f(c*3, e)
print(f(12, 40) * f(40, 72) * f(72, 89))