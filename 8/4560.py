counter = 0
s = 'ТИХОРЕЦК'
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                a = a1 + a2 + a3 + a4
                c = 0
                fr = 0
                if a1 == 'Т': c += 1
                if a2 == 'И': c += 1
                if a3 == 'Х': c += 1
                if a4 == 'О': c += 1
                if c == 2:
                    if a.count('И') + a.count("О") + a.count('Е') == 2:
                        for abcdefghijklmnopqrstuvwxyz in a:
                            if a.count(abcdefghijklmnopqrstuvwxyz) == 0 or a.count(abcdefghijklmnopqrstuvwxyz) == 1:
                                  fr += 1
                        if fr == 4:
                            counter += 1
print(counter)