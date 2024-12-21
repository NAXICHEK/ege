f = open('17.txt')
g = [int(x) for x in f]
c = 0
mm = 0
for i in range(len(g)-1):
    for j in range(i+1, len(g)):
        a = g[i]
        b = g[j]
        if (abs(a-b) % 2 == 0) and ((a % 31 == 0) or (b % 31 == 0)):
            c += 1
            mm = max(mm, a+b)
print(c, mm)