s = '1' + '8'*110
while '1' in s:
    if '18' in s:
        s = s.replace('18', '8881', 1)
    else: s = s.replace('1', '888', 1)
print(sum(map(int, s)))