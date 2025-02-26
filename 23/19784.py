def f(c, e):
    if c < e or c == 28: return 0
    if c == e: return 1
    return f(c-2, e) + (f(c//2, e) if c % 2 == 0 else f(c-3, e))
print(f(98, 1))