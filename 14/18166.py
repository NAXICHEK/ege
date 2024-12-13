def f(x):
    s = ''
    while x > 0:
        s = str(x%5) + s
        x //= 5
    return s
m = 0
for x in range(2, 2026):
    r = f(5**2025 + 5**200 - x)
    m = max(m, r.count('4'))
    if r.count('4') == m:
        print(x) # 1876