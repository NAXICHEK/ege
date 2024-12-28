def f(a, b, m):
    if a+b <= 72: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a-3,b,m-1),
        f(a,b-3,m-1),
        f(a/2,b,m-1),
        f(a,b/2,m-1),
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(23, 1000) if f(50, s, 2) and not f(50, s, 1)])
print('20)', [s for s in range(23, 1000) if f(50, s, 3) and not f(50, s, 1)])