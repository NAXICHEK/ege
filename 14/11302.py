s = '0123456789abcdefghijklmno'
for i in s:
    r = int(f'488926{i}9', 25) + int(f'8378{i}2678', 25) + int(f'6247{i}9', 25) + int(f'4{i}691', 25) + int(f'737{i}9{i}89', 25)
    if r % 24 == 0:
        print(r//24) # 54618873664