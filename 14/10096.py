s = '0123456789abcdefghi'
for i in s:
    r = int(f'98897{i}21', 19) + int(f'2{i}923', 19)
    if r % 18 == 0:
        print(r//18) # 469034148