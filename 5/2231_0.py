a = []
for n in range(1000):
    b = f'{n:b}'
    if n % 2 != 0:
        b = '10' + b + '11'
    else:
        b = '1' + b + '00'
    r = int(b, 2)
    if r > 1023:
        a.append(r)
print(min(a))