m = 0
for i in range(4, 10000):
    s = '8' + '4' * i
    while '11' in s or '444' in s or '8888' in s:
        s = s.replace('11', '4', 1)
        s = s.replace('444', '88', 1)
        s = s.replace('8888', '1', 1)
    m = max(m, sum(map(int, s)))
    print(m)