def f(x):
    s = ''
    d = '0123456789abcdefghijklmnopqrstuvwxyz'
    while x > 0:
        s = d[x%25] + s
        x //= 25
    return s

a = f(3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2 * 25**4 - 2025)
print(a.count('0')) # 10