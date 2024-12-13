g = sorted('МОЛЬ')
c = 0
print(g)
for a1 in 'ЛМО':
    for a2 in g:
        for a3 in g:
            for a4 in g:
                for a5 in g:
                    s = a1 + a2 + a3 + a4 + a5
                    if ('ОЬ' not in s) and ('ЬЬ' not in s):
                        c += 1
print(c)