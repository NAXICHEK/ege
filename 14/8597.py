s = '0123456789abcde'
a = 0
for i in s:
    r = int(f'97968{i}13',19) + int(f'7{i}213',19)
    if r % 11:
        a += int(i, 15)
print(a)