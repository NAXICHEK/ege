def f(c, e):
    if c < e or c == 32: return 0
    if c == e: return 1
    return f(c-1, e) + f(c-5, e)
print(f(42, 23)*f(23, 22)*f(22, 9)) # 1160