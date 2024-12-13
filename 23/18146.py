def f(c, e):
    if c < e or c == 28: return 0
    if c == e: return 1
    if c > e: return f(c-3, e) + f(c//3, e) + f(c//2, e)
print(f(46, 20) * f(20, 3)) # 12