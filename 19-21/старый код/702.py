def f(a, m):
    if (a >= 36) and (a <= 85): return m % 2 == 0
    elif a > 85: return m % 2 != 0
    if m == 0: return 0
    h = [
        f(a+2, m-1),
        f(a*3, m-1)
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)

print('19)', [s for s in range(30,33,2) if f(s, 3)]) # ПВ
print('20)', [s for s in range(8,11,2) if f(s, 5)]) # ПВ
print('21)', [s for s in range(6, 7) if f(s, 6)]) # В