
def f(x):
    s = ''
    while x > 0:
        s = str(x%6) + s
        x //= 6
    return s

for i in range(2031):
    a = f(6**260 + 6**160 + 6**60 - i)
    if a.count('0') == 202:
        print(i) # 1944