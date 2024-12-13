def f(a, b, c, m):
    if ((a >= 20) or (b >= 20)  or (c >= 20)) or (a+b+c >= 25): return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+2,b+2,c+2,m-1),
        f(a*2,b,c,m-1),
        f(a,b*2,c,m-1),
        f(a,b,c*2,m-1)
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 20) if not f(2, 3, s, 1) and f(2, 3, s, 2)]) # 9
print('20)', [s for s in range(1, 20) if not f(2, 3, s, 1) and f(2, 3, s, 3)]) # 2 3
print('21)', [s for s in range(1, 20) if not f(2, 3, s, 2) and f(2, 3, s, 4)]) # 6