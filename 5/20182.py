def cc(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s
a = []
for i in range(1000):
    b = cc(i)
    if sum(map(int, b)) % 2 == 0:
        b = '12' + b[2:] + '0'
    else:
        b = '10' + b[2:] + '2'
    r = int(b, 3)
    if r > 105:
        a.append(i)
print(min(a))