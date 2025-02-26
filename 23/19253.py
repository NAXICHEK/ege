def f(c, e):
    g = 0
    if c > e : return 0
    if c == e: return 1
    return f(c+2, e) + f(c+3, e) + f(c*2, e)
print(f(8, 35) - (f(8, 20) * f(20, 30) * f(30, 35)))