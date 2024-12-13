for i in range(1000):
    s = '3' + '0'*40 + '1'*i + '2'*40
    while '31' in s or '32' in s or '30' in s:
        s = s.replace('31', '223', 1)
        s = s.replace('32', '23', 1)
        s = s.replace('30', '13', 1)
    s = s.replace('3', '0', 1)
    if (sum(map(int, s)) == 111) or (sum(map(int, s)) == 222) or (sum(map(int, s)) == 333) or (sum(map(int, s)) == 444) or (sum(map(int, s)) == 555) or (sum(map(int, s)) == 666) or (sum(map(int, s)) == 777) or (sum(map(int, s)) == 888) or (sum(map(int, s)) == 999):
        print(i)