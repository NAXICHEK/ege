import time
def div(x):
    d =set()
    c = 0
    for i in range(1, int(x**0.5) + 1):
        if (x % i == 0) and (c < 6) and (i % 2 == 1) and ((x//i) % 2 == 1):
            d |= {i, x // i}
            c += 1
    return sorted(d)

for i in range(55000000, 60000000 + 1):
    d = [int(x) for x in div(i) if x % 2 == 1]
    if len(d) == 5:
        print(i, d[4])