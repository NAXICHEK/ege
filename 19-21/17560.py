def f(s, m):
    if s >= 58: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s+1, m-1),
        f(s+4, m-1),
        f(s*2, m-1),
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 58) if not f(s, 1) and f(s, 2)]) # 28
print('20)', [s for s in range(1, 58) if not f(s, 1) and f(s, 3)]) # 14 24
print('20)', [s for s in range(1, 58) if not f(s, 2) and f(s, 4)]) # 23