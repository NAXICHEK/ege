def f(a, c, e):
    if a >= 128 or c > e:return c%2 == e%2
    h = [
        f(a+2, c+1, e),
        f(a+5, c+1, e),
        f(a*2, c+1, e),
    ]
    return any(h) if (c+1) % 2 == e % 2 else all(h)

print([s for s in range(1, 128) if f(s, 0, 2) and not f(s, 0, 1)])
print([s for s in range(1, 128) if f(s, 0, 3) and not f(s, 0, 1)])
print([s for s in range(1, 128) if f(s, 0, 4) and not f(s, 0, 2)])