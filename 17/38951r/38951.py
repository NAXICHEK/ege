f = open('17.txt')
g = [int(x) for x in f]
c = 0
mm = 0
for i in range(len(g)-1):
    a = g[i]
    b = g[i+1]
    if ((a % 3 == 0) or (b % 3 == 0)) and ((a+b) % 5 == 0):
        c += 1
        mm = max(mm, a+b)
print(c, mm)