def f(c, e, p1, p2):
    if c == 20: p1 = 1
    if c == 30: p2 = 1
    if c >= e: return c == e and p1 + p2 == 1
    return f(c+3, e, p1, p2) + f(c+5, e, p1, p2) + f(c*2, e, p1, p2)
print(f(10, 40, 0, 0))