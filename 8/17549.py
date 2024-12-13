a = sorted('ФОКУС')
skolko_xyev_vsego = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    s = a1 + a2 + a3 + a4 + a5
                    skolko_xyev_vsego += 1
                    if s.count('Ф') == 0:
                        if s.count('У') == 2:
                            print(skolko_xyev_vsego)