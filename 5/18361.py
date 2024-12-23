for i in range(10000):
    b = bin(i)[2:]
    if sum(map(int, b)) % 2 == 0: b = '10' + b[2:] + '0'
    else: b = '11' + b[2:] + '1'
    r = int(b, 2)
    if r > 171:
        print(i)
        break