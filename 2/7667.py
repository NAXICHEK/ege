print('a b c d')
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                if 0 == (((a <= b) == c) or (not d) and (d <= (not a))):
                    print(a, b, c, d)