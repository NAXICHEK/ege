s = 'ДЖАВАСКРИПТ'
for j in s:
        if j == 'А' or j == 'И':
            pass
        else: s = s.replace(j, '.')
print(s)
d = 0
for i in s:
    if i != '.':
        d += s.index(f'{i}') + 1
        s = s.replace(i, '.', 1)
        print(d, s)

        # ..А.А...И..
        # 3....А...И..
        # 8........И..
        # 17...........