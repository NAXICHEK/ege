def f(a, b, m):
    if a+b >= 77: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+3, b, m-1),
        f(a, b + 3, m -1),
        f(a * 3, b, m-1),
        f(a, b * 3, m-1)
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 65) if f(12, s, 2)]) # 21
print('20)', [s for s in range(1, 65) if not f(12, s, 1) and f(12, s, 3)]) # 7 18
print('21)', [s for s in range(1, 65) if not f(12, s, 2) and f(12, s, 4)]) # 2