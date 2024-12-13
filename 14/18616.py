def cc10(a, n):
    a = a[::-1]
    s = 0
    for i in range(len(a)):
        s += a[i]*n**i
    return s

for x in range(37):
    a = cc10([12, 5, 9, x, 11, 10, 9, 8, 15], 37) * cc10([14, 3, x, 5, 13, 10, 9, 12, 6], 37)
    if a % 36 == 0:
        print(x, cc10([2,x,1], 37))