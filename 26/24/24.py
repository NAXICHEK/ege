f = open('26_24.txt')
s, n  = map(int, f.readline().split())
a = sorted([int(x) for x in f])
s1 = 0
k = 0
b = 0
for i in range(n):
    if s1 + a[i] <= s:
        s1 += a[i]
        k += 1
        b = a[i]
        a[i] = 0
for i in range(n):
    if a[i] != 0 and s1 - b + a[i] <= s:
        s1 = s1 - b + a[i]
        a[i], b = b, a[i]
print(k, b)