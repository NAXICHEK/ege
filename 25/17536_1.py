def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: d |= {i, x//i}
    return max(sorted(d)) + min(sorted(d)) if len(d) > 1 else 0
c = 0
for i in range(800000, 1000000000):
    m = str(div(i))
    if m[-1] == '4' and c <= 4:
        print(i, m)
        c += 1