def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i == 0:
            d |= {i, x//i}
    return sorted(d)

for i in range(500000, 600000):
    d = [int(x) for x in div(i) if x != 8 and str(x)[-1:] == '8']
    if len(d) != 0:
        print(i, d[0])