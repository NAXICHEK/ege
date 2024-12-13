def f(c, e):
    if c > e or c == 21: return 0
    if c == e: return 1
    return f(c+2, e) + f(c+3, e) + f(c*2, e)
print(f(7, 14)*f(14,32)) # 160