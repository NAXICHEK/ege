a = []
for i in range(100):
    b = f'{i:b}'
    if b.count('1') % 2 == 0: b = b + '11'
    else: b = b + '00'
    r = int(b, 2)
    if r > 54:
        a.append(r)
print(min(a))