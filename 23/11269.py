def f(c, e):
    if c < e: return 0
    if c == e: return 1
    return f(c-3, e) + f(c-1, e)
print(f(34, 25)*f(25, 22) * f(22, 18)) # 114