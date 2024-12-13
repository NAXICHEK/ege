a = sorted('ГИРЛЯНДА')
k = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    for a6 in a:
                        k += 1
                        s = a1 + a2 + a3 + a4 + a5 + a6
                        if a1 != 'Я':
                            if s.count('Д') == 3:
                                if k % 2 == 0:
                                    print(k)