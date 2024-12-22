def f(a, m):
    if a >= 469: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+5, m-1),
        f(a*3, m-1),
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print([x for x in range(1, 469) if not f(x, 1) and f(x, 2)])
print([x for x in range(1, 469) if not f(x, 1) and f(x, 3)])
print([x for x in range(1, 469) if not f(x, 2) and f(x, 4)])