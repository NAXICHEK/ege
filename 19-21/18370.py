def f(a, m):
    if a >=313: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+2, m-1),
        f(a+3, m-1),
        f(a*3, m-1),
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', sum([x for x in range(1, 313) if not f(x, 1) and f(x, 2)]))
print('20)', [x for x in range(1, 313) if not f(x, 1) and f(x, 3)])
print('21)', sum([x for x in range(1, 313) if not f(x, 2) and f(x, 4)]))