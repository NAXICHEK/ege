def f(a, b, m):
    if a+b >= 455: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+1,b,m-1),
        f(a,b+1,m-1),
        f(a*2,b,m-1),
        f(a,b*2,m-1),
    ]
    return any(h) if (m - 1) % 2 == 0 else any(h)