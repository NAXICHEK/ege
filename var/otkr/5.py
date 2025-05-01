a = []
for i in range(1000):
    b = f'{i:b}'
    b = b[:-1] + str(sum(map(int, b)) % 2)
    b = b[:-1] + str(sum(map(int, b)) % 2)
    r = int(b, 2)
    if r > 253:
        a.append(i)
print(sorted(a))


b = '111000'
b = b[:-1] + str(sum(map(int, b)) % 2)
print(b)