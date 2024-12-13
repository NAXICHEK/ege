def f(c, e):
    if c < e: return 0
    if c == e: return 1
    if c > e: return f(c-2, e) + f(c//2, e)
print(f(32, 14)* f(14,1)) # 54