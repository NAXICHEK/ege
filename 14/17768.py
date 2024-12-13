def f(x):
    s = ''
    while x > 0:
        s = str(x % 4) + s
        x //= 4
    return s
a = 4**644 + 4**322 + 16**35 - 64**3

d = f(a)
print(d.count('3')) # 61