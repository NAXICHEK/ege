def f(c, e):
    if c < e: return 0
    if c == e: return 1
    return f(c-1, e) + f(c-2, e) + f(c//4, e)
print(f(26, 20)*f(20,3)) # 34749