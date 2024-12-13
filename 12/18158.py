m = 0
for i in range(3, 10000):
    s = '4' + '1'*i
    while '411' in s or '1111' in s:
        s = s.replace('411', '14', 1)
        s = s.replace('1111', '1', 1)
    a = sum(map(int, s))
    m = max(m, a)
    print(m)