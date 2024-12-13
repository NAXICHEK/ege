def f(c, e):
    if c > e or c == 16: return 0
    if c == e: return 1
    return f(c+1, e) + f(c+3, e) + f(c**2, e)
print(f(3, 20) * f(20, 26)) # 936