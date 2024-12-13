s = sorted('ГРАНТ')
c = 0
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    for a6 in s:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        c += 1
                        if a == 'ГРАНАТ':
                            print(c) # 5055