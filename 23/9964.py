def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e: return f(c+1, e) + f(c*3, e) + f(c+5, e)