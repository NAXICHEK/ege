def f(c, e):
    if c > e or c == 11 or c == 12: return 0
    if c == e: return 1
    return f(c+1, e) + f(c*2, e) + f(c**2, e)
print(f(2, 10) * f(10, 40)) # 22