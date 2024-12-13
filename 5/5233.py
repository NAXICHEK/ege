
a = set()
for i in range(100, 201):
    b = bin(i)[2:]
    if sum(map(int, b)) % 2 == 0:
        b = '10' + b[:-2] + '00'
    else:
        b = '11' + b[:-2] + '11'
    r = int(b, 2)
    if r % 3 == 0:
        a.add(r)
print(sum(a)) # 11400