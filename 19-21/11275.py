def fn(a, b, m):
    if a+b >= 131: return m % 2 == 0
    if m == 0: return 0
    h = [
        fn(a+2, b, m-1),
        fn(a, b+2, m-1),
        fn(a*2, b, m-1),
        fn(a, b*2, m-1),
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print([s for s in range(1, 123) if not fn(11, s, 1) and fn(11, s, 2)]) # 30
print([s for s in range(1, 123) if not fn(11, s, 1) and fn(11, s, 3)]) # 54 57
print([s for s in range(1, 123) if not fn(11, s, 2) and fn(11, s, 4)]) # 52