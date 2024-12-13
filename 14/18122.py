def pyat(x):
    s = ''
    while x > 0:
        s = str(x%5) + s
        x //= 5
    return s
for x in range(5556):
    v = pyat(5 ** 150 + 5 ** 135 - x)
    if v.count('4') == 134:
        print(x) # 3126