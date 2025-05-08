def f(s, c, end):
    if s >= 67 or c > end: return c%2 == end%2
    h = [
        f(s+1, c+1, end),
        f(s+4, c+1, end),
        f(s*3, c+1, end),
    ]
    return any(h) if (c+1)%2 == end%2 else all(h)


print([s for s in range(1, 67) if f(s, 0, 2) and not f(s, 0, 1)])
print([s for s in range(1, 67) if f(s, 0, 3) and not f(s, 0, 1)])
print([s for s in range(1, 67) if f(s, 0, 4) and not f(s, 0, 2)])