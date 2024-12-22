def f(c, e, l):
    if c > e: return 0
    if c == e: return 1
    if l != 2: return f(c+2, e, 1) + f(c**2, e, 2) + f(c*3, e, 3)
    else: return f(c+2, e, 1) + f(c*3, e, 3)

print(f(2, 64, 0))