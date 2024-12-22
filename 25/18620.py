def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: d |= {i, x//i}
    if len(d) >= 2: return sum(sorted(d)[len(d)-2:])
    else: return 0
for i in range(112500000, 112550000+1):
    m = div(i)
    if str(m)[-4:] == '1214':
        print(i)