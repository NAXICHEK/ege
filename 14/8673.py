s = '01234567'
for i in s:
    r = int(f'2567{i}3',8) + int(f'1{i}24',8)
    if r % 7 == 0:
        print(r//7) # 12929