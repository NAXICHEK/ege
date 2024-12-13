def div(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
         d |= {i, x//i}
    return sorted(d)

for i in range(190201, 190260 + 1):
    d = [int(l) for l in div(i) if l%2==0]
    if len(d) == 4:
        print(d[3], d[2])