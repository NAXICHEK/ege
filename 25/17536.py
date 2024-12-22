def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: d |= {i, x//i}
    if len(d) > 0: return max(sorted(d)) + min(sorted(d))
c = 0
for i in range(800000, 10000000000):
    m = div(i)
    if str(m)[-1] == '4' and c <= 4:
        print(i, m)
        c += 1