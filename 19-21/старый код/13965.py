def f(a, b, m):
    if a * b >= 541: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+10,b,m-1),
        f(a,b+10,m-1),
        f(a*2,b,m-1),
        f(a,b*2,m-1)
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 91) if not f(6, s, 1) and f(6, s, 2)]) # 17
print('20)', [s for s in range(1, 91) if not f(6, s, 1) and f(6, s, 3)]) # 11 23
print('21)', [s for s in range(1, 91) if not f(6, s, 2) and f(6, s, 4)]) # 6