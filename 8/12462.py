k = 0
for a1 in '123456789abcdef':
    for a2 in '0123456789abcdef':
        for a3 in '0123456789abcdef':
            for a4 in '0123456789abcdef':
                for a5 in '0123456789abcdef':
                    if a1>a2>a3>a4>a5:
                        k+=1
for b1 in '123456789abcdef':
    for b2 in '0123456789abcdef':
        for b3 in '0123456789abcdef':
            if b1>b2>b3:
                k+=1
print(k)