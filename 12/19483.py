m = 1000000000
for i in range(3, 1000):
    s = '2' + '5' * i
    while '25' in s or '355' in s or '555' in s:
        s = s.replace('25', '5', 1)
        s = s.replace('355', '522', 1)
        s = s.replace('555', '3', 1)
    if s.count('2') == 10:
        print(i)