def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: d |= {i, x//i}
    if len(d) > 1: return int(sum(d)/len(d))
    else: return 0
c = 0
for i in range(700000, 1, -1):
    m = div(i)
    if str(m)[-3:] == '313' and c <= 6:
        print(i, m)
        c += 1