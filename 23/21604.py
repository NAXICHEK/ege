def f(c, e):
    if c < e or c == 24: return 0
    if c == e: return 1
    return f(c-1, e) + f(c-4, e) + f(c//2, e)
print(f(34, 30) * f(30, 20) * f(20, 9))