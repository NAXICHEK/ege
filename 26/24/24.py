f = open('26_24.txt')
f.readline()
s, n = 8200, 970
a = sorted([int(x.replace('\n', '')) for x in f])
print(a)
s1 = 0
b = 0
c = 0
for i in range(n):
    if s1 + a[i] <= s:
        s1 += a[i]
        c += 1
        a.pop(i)
print(s1, c)