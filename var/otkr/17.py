f = open('17_21903.txt')
g = [int(x.replace('\n', '')) for x in f]
mini = min(x for x in g if str(x)[-1] == '5' and str(x)[-2] == '1' and len(str(abs(x))) == 3)
cc = 0
m = 1000000000
for i in range(len(g)-2):
    a, b, c = g[i], g[i+1], g[i+2]
    if a >= 0 and b >= 0 and c >= 0:
        if max(a, b, c) * min(a, b, c) > mini ** 2:
            cc += 1
            m = min(m, max(a, b, c) * min(a, b, c))
    elif a <= 0 and b <= 0 and c <= 0:
        if max(a, b, c) * min(a, b, c) > mini ** 2:
            cc += 1
            m = min(m, max(a, b, c) * min(a, b, c))
print(cc, m)