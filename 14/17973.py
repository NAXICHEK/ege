
for x in range(24):
    s = '0123456789ABCDEFGHIJKLMN'
    r = int(f'12{s[x]}734', 24) + int(f'8{s[x]}95{s[x]}3', 24) + int(f'24{s[x]}796', 24)
    if r % 23 == 0:
        print(r//23) # 4166339