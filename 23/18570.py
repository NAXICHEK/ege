def f(c, e):
    if c > e or c == 16: return 0
    if c == e: return 1
    return f(c+1, e) + f(c*2, e) + f(c*3, e)

print(f(1, 14)*f(14,50)) # 192