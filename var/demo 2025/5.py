a = []
for i in range(13):
    b = f'{i:b}'
    if i % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    r = int(b, 2)
    a.append(r)
print(max(a))
print(a)
