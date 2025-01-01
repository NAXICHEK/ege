a = []

for i in range(1, 50):
    b = f'{i:b}'
    if sum(map(int, b)) % 2 == 0:
        b = '11' + b[2:] + '0'
    else:
        b = '10'+ b[2:] + '1'
    r = int(b, 2)
    a.append(r)
print(max(a))