from time import process_time

c = 0
a = []
for n in range(136314890):
    s = ''
    b = f'{n:b}'
    ed = b.count('1')
    nu = b.count('0')
    edb = f'{ed:b}'
    nub = f'{nu:b}'
    if nub != 0:
        s = str(nub) + str(edb)
        r = int(s, 2)
        print(r, n)
        if r == 214:
            a.append(n)
            print('!!!!!!!!')
print(min(a), process_time())