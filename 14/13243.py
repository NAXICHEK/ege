def f(x):
    s = ''
    d = '0123456789abcdefghijklmnopqrstuvwxyz'
    while x > 0:
        s = d[x%18] + s
        x //= 18
    return s
for i in range(1000):
    r = int(f(int(f'1{i}253', 18)), 18) + int(f(int(f'32{i}8', 18)), 18)
    if r % 7 == 0:
        print(int(r/7)) # 19367