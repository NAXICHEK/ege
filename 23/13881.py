def f(c, e):
    if c > e or c == 20: return 0
    if c == e: return 1
    return f(c+1, e) + f(c+3, e) + f(c**2, e)
print(f(3, 23)*f(23,25)) # 516