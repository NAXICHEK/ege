for s in range(12, 35):
    for p in range(30, 37):
        rez = int(f'R4', p-1) + int(f'B0', s+2) + int(f'T3NK4', p)
        if rez == 23593399:
            print(s*p)