def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: d |= {i, x//i}
    return sorted(d)

for i in range(700000, 10000000):
    d = [x for x in div(i) if str(x)[-1] == '7' and x != 7]
    if len(d) != 0:
        print(i, min(d))