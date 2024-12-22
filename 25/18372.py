def div(x):
    d = set()
    d |= {1}
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return int(sum(d)/len(d))
c = 0
for i in range(770000, 0, -1):
    a = div(i)
    if str(a)[-2:] == '12' and c <= 4:
        print(i, a)
        c += 1