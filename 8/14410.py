s = sorted('СОЛНЦЕ')
c = 0
d = 1
for a1 in sorted('СЛНЦ'):
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    for a6 in s:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        if a.count('Ц') == 2:
                            if d % 2 == 0:
                                c += 1
                        d += 1
print(c) # 4025