counter = 0
for a in 'АБВГ':
    for b in 'АБВГ':
        for c in 'АБВГ':
            for d in 'АБВГ':
                for e in 'АБВГ':
                    s = a+b+c+d+e
                    if s.count('А') == 1:
                        counter += 1
print(counter)