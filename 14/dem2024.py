def f(x):
    s = ''
    d = '0123456789abcdefghijklmnopqrstuvwxyz'
    while x > 0:
        s = d[x%19] + s
        x //= 19
    return s

for i in 'abcdefghijklmnopqrstuvwxyz':
    r = int(f(int(f'98897{i}21', 19)),19) + int(f(int(f'2{i}923', 19)),19)
    if r % 18 == 0:
        print(r//18)