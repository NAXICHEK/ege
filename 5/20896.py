a = []
for n in range(1000):
    b = f'{n:b}'
    if sum(map(int, b)) % 2 == 0:
        b = b + '0'
        b = b[:-2] + '10'
    else:
        b = b + '1'
        b = b[:-2] + '11'
    r = int(b, 2)
    if r > 19:
        print(n)
        break