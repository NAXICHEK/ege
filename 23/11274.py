def f(c, e):
    if c < e: return 0
    if c == e: return 1
    return f(c-3, e) + f(c-1, e) + f(c//2, e)
print(f(39, 19) * f(19, 16) * f(16, 7)) # 56320