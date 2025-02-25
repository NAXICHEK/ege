m = 10000000000
for i in range(100):
    b = f'{i:b}'
    if i % 2 == 0: b = b + b[0:3]
    else: b = '1' + b + '01'
    r = int(b, 2)
    if r > 600:
        m = min(m, r)
print(m)