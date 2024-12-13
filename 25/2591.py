def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)
def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
f = []
for i in range(125697, 125721 + 1):
    d = [int(x) for x in div(i) if p(x)]
    if len(d) > 1:
        for j in d:
            for k in d:
                if j * k == i:
                    f.append(j)
                    f.append(k)
                    print(min(d), max(d), max(d) * min(d))
                    f.clear()