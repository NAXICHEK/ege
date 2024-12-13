def f(a, m):
    if a >= 63: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+1, m-1),
        f(a+4, m-1),
        f(a*5, m-1),
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 63) if not f(s, 1) and f(s, 2)]) # 3
print('19)', [s for s in range(1, 63) if not f(s, 1) and f(s, 3)]) # 8 12
print('19)', [s for s in range(1, 63) if not f(s, 2) and f(s, 4)]) # 3