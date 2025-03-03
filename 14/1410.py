def cc(x):
    s = ''
    while x > 0:
        s = str(x % 4) + s
        x //= 4
    return s

r = cc(4**625 - 2*311 + 2**571 - 48)
print(r.count('1'))