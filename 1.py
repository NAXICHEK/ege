a = int(input())
d = 0
c = 0
for i in range(a):
    b = int(input())
    if b > 0:
        d += b
        c += 1
print(d/c)
print(c)