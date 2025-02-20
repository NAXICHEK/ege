def cc(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s

for i in range(1000):
    b = cc(i)
    if sum(map(int, b)) % 2 == 0:
        b = '12' + b[1:] + '0'