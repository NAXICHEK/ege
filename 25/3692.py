# 123*567
for i in range(1000000, 10**9):
    a = str(i)
    if a[:3] == '123':
        if a[-3:] == '567':
            if i % 169 == 0:
                print(i, i//169)