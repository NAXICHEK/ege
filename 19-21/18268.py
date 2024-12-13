def f(a, b, m):
    if a+b <= 72: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a-3, b, m-1),
        f(a, b-3, m-1),
        f((a+1)//2, b, m-1),
        f(a, (b+1)//2, m-1)
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(23, 1000) if f(50, s, 2)]) # 94
print('20)', [s for s in range(23, 1000) if not f(50, s, 1) and f(50, s, 3)]) # 51 100
print('21)', [s for s in range(23, 1000) if not f(50, s, 2) and f(50, s, 4)]) # 103
