skolko = 0
for a1 in '123456789abcde':
    for a2 in '0123456789abcde':
        for a3 in '0123456789abcde':
            for a4 in '0123456789abcde':
                for a5 in '0123456789abcde':
                    s = a1 + a2 + a3 + a4 + a5
                    if s.count('8') == 1:
                        if s.count('a') + s.count('b') + s.count('c') + s.count('d') + s.count('e') >= 2:
                            skolko += 1
print(skolko)