a = []
m = 0
for n in range(1000):
    b = f'{n:b}'
    if n % 2 == 0: b = b.replace('0','1')
    else:
        b = b.replace('1', '!', 1)
        b = b.replace('1', '00')
        b = b.replace('!', '1')
    r = int(b, 2)
    if r == 512:
        print(n)