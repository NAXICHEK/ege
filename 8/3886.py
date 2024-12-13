a = sorted('КЕГЭ')
a.append('0')
a.append('2')
a.append('3')
c = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                s = a1+a2+a3+a4
                c += 1
                if a1 in '023':
                    if 'КК' not in s:
                        if 'ЕЕ' not in s:
                            if 'ГГ' not in s:
                                if 'ЭЭ' not in s:
                                    if '22' not in s:
                                        if '00' not in s:
                                            if '33' not in s:
                                                print(c)
print(c)
print(a)