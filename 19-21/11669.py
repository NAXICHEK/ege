def f(s, m):
    if s <= 116: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(s-7,m-1),
        f(s//3,m-1),
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', max([s for s in range(117, 10000) if not f(s, 2) and f(s, 3)])) # 3158
print('20)', min([s for s in range(117, 10000) if not f(s, 1) and f(s, 3)]), max([s for s in range(117, 10000) if not f(s, 1) and f(s, 3)])) # 361 1082
print('21)', max([s for s in range(117, 10000) if not f(s, 2) and f(s, 4)])) # 1080