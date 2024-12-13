a = sorted('ПРЕСТОЛ')
counter = 0
counter2 = 0
b = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    s = a1 + a2 + a3 + a4 + a5
                    counter += 1
                    if (s[-1] == 'У' or s[-1] == 'О') and (s.count('П') + s.count('Р') + s.count('С') + s.count('Т') + s.count('Л') <= 3):
                        if counter % 2 == 1:
                            counter2 += 1
print(counter2)