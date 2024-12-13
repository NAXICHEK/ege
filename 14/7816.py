a = '0123456789abcde'
for i in a:
    r = int(f'97531{i}19', 15) + int(f'3{i}519', 15)
    if r % 11 == 0:
        print(r//11)