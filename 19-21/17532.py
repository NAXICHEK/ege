def f(a,b,m):
    if a+b >= 65: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+1, b, m-1),
        f(a, b+1, m-1),
        f(a*3, b, m-1),
        f(a, b*3, m-1)
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 59) if not f(6, s, 1) and f(6, s, 2)]) # 7
print('20)', [s for s in range(1, 59) if not f(6, s, 1) and f(6, s, 3)]) # 10 19
print('21)', [s for s in range(1, 59) if not f(6, s, 2) and f(6, s, 4)]) # 18