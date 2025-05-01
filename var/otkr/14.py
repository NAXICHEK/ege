def f(x):
    s = ''
    while x > 0:
        s = str(x%7) + s
        x //= 7
    return s

for x in range(2301):
    if f(7**350 + 7**150 - x).count('0') == 200:
        print(x)