f = open('24_17535.txt').read()
f = f.replace('CD', ' ').split()
a = []
for i in f:
    a.append(len(i))
m = 0
for i in range(len(a)):
    b = sum(a[0:160])
    m = max(b, m)
    a.pop(0)
print(m)