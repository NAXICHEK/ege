def f(a, b, c, e):
    if a+b >= 81 or c > e: return c% 2 == e%2
    h = [
        f(a+1, b, c+1, e),
        f(a, b+1, c+1, e),
        f(a, b*2, c+1, e),
        f(a*2, b, c+1, e),
    ]
    return any(h) if (c+1) % 2 == e%2 else all(h)
print([s for s in range(1, 74) if f(s, 7, 0, 2) and not f(s, 7, 0 ,1)]) # 19
print([s for s in range(1, 74) if f(s, 7, 0, 3) and not f(s, 7, 0 ,1)]) # 19
print([s for s in range(1, 74) if f(s, 7, 0, 4) and not f(s, 7, 0 ,2)]) # 19