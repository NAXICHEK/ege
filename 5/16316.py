for i in range(1, 100):
    n = i
    b = bin(i)[2:]
    if int(n) % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    r = int(b, 2)
    if r > 516:
        print(i) # 65