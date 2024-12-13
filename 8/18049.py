counter = 0
for a1 in '13578':
    for a2 in '012345678':
        for a3 in '012345678':
            for a4 in '012345678':
                for a5 in '012345678':
                   for a6 in '012345678':
                       for a7 in '012345678':
                           s = a1 + a2 + a3 + a4 + a5 + a6 + a7
                           if s[-1] != s[-2] or s[-2] != s[-3]:
                               counter += 1
print(counter)