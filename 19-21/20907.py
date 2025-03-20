def f(a, b, m):
    if a + b >= 81: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+1, b, m-1),
        f(a, b+1, m-1),
        f(a*2, b, m-1),
        f(a, b*2, m-1),
         ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print([s for s in range(2, 74) if f(7, s, 2) and not f(7, s, 1)]) # 19
print([s for s in range(2, 74) if f(7, s, 3) and not f(7, s, 1)]) # 33 36
print([s for s in range(2, 74) if f(7, s, 4) and not f(7, s, 2)]) # 32