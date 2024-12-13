for x in '0123456789abcde':
    f = int(f'123{x}5', 15) + int(f'1{x}223', 15)
    if f % 14 == 0:
        print(f//14)

for x in '0123456789abcde':
    r = int('123' + str(x) + '5', 15) + int('1' + str(x) + '233', 15)
    if r % 14 == 0:
        print(r//14)
