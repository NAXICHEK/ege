# def f(x):
#     s = ''
#     d = '0123456789abcdefghijklmnopqrstuvwxyz'
#     while x > 0:
#         s = d[x % 25] + s
#         x // 25
#     return s

for x in '0123456789abcdefghijklmno':
    r = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if r % 24 == 0:
        print(r//24)