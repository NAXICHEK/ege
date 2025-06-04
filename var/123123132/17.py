f = open('17_19249.txt')
g = [int(x) for x in f]
cc = 0
m = 1000000000000000000000000000000000000000000
mini = max([x for x in g if len(str(abs(x))) == 5 and str(x)[-2:] == '43'])
print(mini)
for i in range(len(g)-2):
    a = g[i]; b = g[i+1]; c = g[i+2]
    if (len(str(abs(a))) == 5 and str(a)[-2:] == '43') or (len(str(abs(b))) == 5 and str(b)[-2:] == '43') or (len(str(abs(c))) == 5 and str(c)[-2:] == '43'):
        if a**2 + b**2 + c**2 <= mini**2:
            cc += 1
            m = min(m, a**2 + b**2 + c**2)
print(cc, m)