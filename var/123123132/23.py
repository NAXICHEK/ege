def f(c, e):
    if c < e or c == 24: return 0
    if c == e: return 1
    return f(c-1, e) + f(c-6, e) + f(c//2, e)
print(f(34, 29)*f(29,19)*f(19, 6))