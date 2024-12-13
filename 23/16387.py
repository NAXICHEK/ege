def f(c, e):
    if c > e or c == 16: return 0
    if c == e: return 1
    return f(c+1, e) + f(c+2, e) + f(c*3, e)
print(f(2, 9)*f(9,18)) # 325