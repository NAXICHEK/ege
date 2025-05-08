# def f(a, m):
#     if a >= 82: return m % 2 == 0
#     if m == 0: return 0
#     h = [
#         f(a+10, m-1),
#         f(a*2, m-1),
#     ]
#     return any(h) if (m-1) % 2 == 0 else all(h)
#
# print('19)', [s for s in range(1, 82) if f(s, 1) and not f(s, 2)])
print('19)', [s for s in range(1, 82) if any((s+10 >= 72 and s+10 < 82) or (s*2 >= 72 and s*2 < 82) for s in [s])][0])