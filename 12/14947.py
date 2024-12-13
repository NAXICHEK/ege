m = 0
for i in range(4, 10000):
    s = '1' + '9' * i
    while '19' in s or '49' in s or '999' in s:
        s = s.replace('19', '9', 1)
        s = s.replace('49', '91', 1)
        s = s.replace('999', '4', 1)
    m = max(m, sum(map(int, s)))
    print(m)