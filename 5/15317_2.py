a = []
ii = []
for i in range(1, 1000):
    b = bin(i)[2:]
    if int(b) % 2 == 0:
        b = b + '01'
    else:
        b = '1' + b + '1'
    r = int(b, 2)
    if r > 156:
        print(i)