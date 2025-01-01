a = []

for i in range(1, 10000):
    b = f'{i:b}'
    if sum(map(int, b)) % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '1' + b[:-2] + '10'
    r = int(b, 2)
    if r < 224:
        print(i)