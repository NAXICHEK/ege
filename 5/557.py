a = []
for i in range(1000):
    b = f'{i:b}'
    b = b + b[-1]
    if b.count('1') % 2 == 0:
        b = b + '0'
    else:
        b = b + '1'
    b = b + '0'
    r = int(b, 2)
    if r > 144:
        a.append(r)
print(min(a))