a = []
for i in range(1, 100):
    b = bin(i)[2:]
    if i % 2 == 1:
        b = '10' + b + '11'
    else:
        b = '1' + b + '00'
    r = int(b, 2)
    if r > 1023:
        a.append(r)
print(sorted(a))