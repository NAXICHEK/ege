def f(c, e):
    if c < e or c == 36 or c == 100: return 0
    if c == e: return 1
    return f(c//2, e) + f(c//3, e) + f(c-3, e)
print(f(163, 45)*f(45, 3)) # 690