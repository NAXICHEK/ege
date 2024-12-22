def f(c, e):
    if c < e or c == 7: return 0
    if c == e: return 1
    return f(c-1, e) + f(c-3, e) + f(c//2, e)
print(f(19, 10)*f(10, 3))