def f(c, m):
    if c >= 132: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(c+3, m-1),
        f(c+6, m-1),
        f(c*3, m-1)
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print([s for s in range(1, 132) if f(s, 2) and not f(s, 1)])
print([s for s in range(1, 132) if f(s, 3) and not f(s, 1)])
print([s for s in range(1, 132) if f(s, 4) and not f(s, 2)])