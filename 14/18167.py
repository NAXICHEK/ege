def f(x):
    s = ''
    while x > 0:
        s = str(x%6) + s
        x //= 6
    return s

for x in range(1, 10001):
    r = f(6**900 + 6**10 - x)
    if r.count('3') == r.count('5'):
        print(x) # 9591