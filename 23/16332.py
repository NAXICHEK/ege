def f(c, e):
    if c > e: return 0
    if c == e: return 1
    return f(c+1, e) + f(c+2, e) + f(c*2, e)
print(f(4, 11)*f(11,13)*(f(13,15))) # 100