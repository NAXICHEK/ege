def f(a, m):
    if a <= 19: return m%2 == 0
    if m == 0: return 0
    h = [
        f(a-2, m-1),
        f(a-5, m-1),
        f(a//3, m-1),
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print([x for x in range(20, 100) if f(x, 2) and not f(x, 1)]) # 60
print([x for x in range(20, 100) if f(x, 3) and not f(x, 1)]) # 60