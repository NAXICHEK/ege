from itertools import *
a = []
c = 0
for i in product('ЯОА', repeat = 2):
    s = ''.join(i)
    a.append(s)
for x in product('ЯРОСЛАВ', repeat = 5):
    s = ''.join(x)
    fl = 1
    fll = 1
    for p in s:
        if s.count(p) > 1:
            fl = 0
    if fl:
        if s.count('Р') + s.count('С') + s.count('Л') + s.count('В') > s.count('Я') + s.count('О') + s.count('А'):
            for p in a:
                if p in s:
                    fll = 0
            if fll:
                c += 1
print(c) # 1224