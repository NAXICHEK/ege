f = open('17_17636.txt')
g = [int(x) for x in f]
m = max(x for x in g if (str(x)[-1] == '3') and (len(str(abs(x))) == 3))
maxi = 0
co = 0
for i in range(len(g)-2):
    a = g[i]
    b = g[i+1]
    c = g[i+2]
    if ((str(a)[-1] == '3') and (len(str(abs(a))) == 3)) or ((str(b)[-1] == '3') and (len(str(abs(b))) == 3)) or ((str(c)[-1] == '3') and (len(str(abs(c))) == 3)):
        if a + b + c < m:
            co += 1
            maxi = max(maxi, a + b + c)
print(co)
print(maxi)