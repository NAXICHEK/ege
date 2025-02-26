def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c+2, e) + f(c*4, e)
print(f(3, 200) * f(200, 510))