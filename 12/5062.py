from itertools import product, repeat


def f(t):
    s = str(t)
    while '00' not in s:
        s = s.replace('011', '20', 1)
        s = s.replace('022', '10', 1)
        s = s.replace('02', '110', 1)
        s = s.replace('01', '220', 1)
    return s
    
for i in range(10, 50):
    print(i, 'i')
    for j in range(100):
        for x in product('12', repeat=i):
            s = ''.join(x)
            g = '0' + str(s)*j + '0'
            if g.count('2') >= 70:
                pass
            if g.count('1') == 47:
                if g.count('2') < 70:
                    print(g.count('2'))