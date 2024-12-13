def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e: return f(c+2, e) + f(c+5, e) + f(c**2, e)
print(f(4, 34) + f(4, 31)) # 319