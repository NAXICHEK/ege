def f(a, b, m):
    if a+b >= 107: return m % 2 == 0
    # if a+b < 170: return m % 2 != 0
    if m == 0: return 0
    h = [
        f(a+10, b, m-1),
        f(a, b + 10, m-1),
        f(a*2, b, m-1),
        f(a, b*2, m-1)
    ]
    return any(h) if (m-1) % 2 == 0 else any(h)

print('19)', [s for s in range(1,101) if not f(5, s, 1) and f(5, s, 2)])