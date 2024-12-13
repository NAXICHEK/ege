def cc(x, y):
    s = ''
    s = str(x % y) + s
    x = x // y
    return s
a = []
g = []
for i in range(1, 100):
    b = cc(i, 3)