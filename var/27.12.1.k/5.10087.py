a = []
for i in range(1000):
    b = f'{i:b}'
    if i % 3 == 0: b = b + b[-3:]
    else: b = b + f'{((i%3)*3):b}'
    r = int(b, 2)
    if r > 151: a.append(r)
print(min(a))