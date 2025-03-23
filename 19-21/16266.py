def f(a, m):
    if a < 20: return m % 2 == 0
    if m == 0: return 0
    h = []
    if a % 3 == 0:
        h = [f(a-10, m-1)]
    elif a % 5 == 0:
        h = [f(a//2, m-1)]
    else:
        h = [
            f(a-10, m-1),
            f(a//2, m-1)
        ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print([s for s in range(31, 100) if f(s, 4) and not f(s, 2)])
print([s for s in range(31, 100) if f(s, 3) and not f(s, 1)])
print([s for s in range(31, 100) if f(s, 4) and not f(s, 2)])