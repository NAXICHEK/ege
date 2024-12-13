def pivo(x):
    d = set()
    for i in range(2, int(x*0.5) + 1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)
def funkciya_proveryashaya_prostoe_li_chislo(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x*0.5) + 1))

c = 0
for i in range(1_273_547, 1_273_547+10000+1):
    d = pivo(i)
    m = sum(d)
    g = m % 100000
    if funkciya_proveryashaya_prostoe_li_chislo(g):
        print(i, m)
        c += 1