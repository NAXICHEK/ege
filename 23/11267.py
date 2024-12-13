def f(c, e):
    if c < e or c == 35: return 0
    if c == e: return 1
    return f(c//3, e) + f(c-2, e) + f(c-5, e)
print(f(41, 37)*f(37, 8)) # 59