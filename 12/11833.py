m = 0
for i in range(4, 10000):
    s = '5' + '7' * i
    while '57' in s or '877' in s or '777' in s:
        s = s.replace('57', '7', 1)
        s = s.replace('877', '75', 1)
        s = s.replace('777', '8', 1)
    m = max(m, sum(map(int, s)))
    print(m)#59