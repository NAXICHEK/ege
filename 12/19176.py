s = '*' * 200
c = 0
while '****' in s or '???' in s:
    if '****' in s:
        s = s.replace('****', '???', 1)
        c += 3
    s = s.replace('??', '*', 1)
print(c)