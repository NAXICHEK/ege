s = '01234567'
c = 0
for a1 in '1234567':
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    for a6 in s:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        if a.count('6') == 1:
                            if (int(a1) % 2 == 0 and int(a2) % 2 == 1 and int(a3) % 2 == 0 and int(a4) % 2 == 1 and int(a5) % 2 == 0 and int(a6) % 2 == 1) or (int(a1) % 2 == 1 and int(a2) % 2 == 0 and int(a3) % 2 == 1 and int(a4) % 2 == 0 and int(a5) % 2 == 1 and int(a6) % 2 == 0):
                                c += 1
print(c)