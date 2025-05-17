for n in range(1000):
    b = f'{n:b}'
    if sum(map(int, b)) % 2 == 0: b = '10' + b[2:] + "0"
    else: b = '11' + b[2:] + "1"
    r = int(b, 2)
    if r > 480:
        print(n)
        break