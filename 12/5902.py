from itertools import product, repeat
m = 0
for x in product('1234', repeat = 100):
    s = ''.join(x)
    s = '>' + s
    if s.count('1') == 50 and s.count('2') == 30 and s.count('3') == 10 and s.count('4') == 10:
        while '>12' in s or '>13' in s or '>41' in s or '>31' in s:
            s = s.replace('>12', '32>', 1)
            s = s.replace('>31', '21>', 1)
            s = s.replace('>13', '41>', 1)
            s = s.replace('>41', '23>', 1)
        m = max(m, sum(map(int, s)))
        print(m)
print(m, 'конец')