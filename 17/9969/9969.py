f = open('17_9969.txt')
g = [int(x) for x in f]
r = [int(x) for x in g if len(set(str(x))) == 5]
m = max(r)
c = 0
def f(a):
    return (a**0.5)**2 == float(a)

for i in range(len(g)-2):
    a = g[i]; b = g[i+1]; c = g[i+2]
    if f(a) == 1 and f(b) == 0 and f(c) == 0:
        if b + c >= m:
            c += 1
    elif f(a) == 0 and f(b) == 1 and f(c) == 0:
        if a + c >= m:
            c += 1
    elif f(a) == 0 and f(b) == 0 and f(c) == 1:
        if a + b >= m:
            c += 1
print(c)
s = '123'
