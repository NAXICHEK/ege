f = open('17 (2)_7718.txt')
g = [int(x) for x in f]
counter = 0
counter1 = 0
m = 0
m1 = 0
for i in range(len(g)-1):
    for j in range(i+1, len(g)):
        a = g[i]
        b = g[j]
        if (((a+b)%18 == 0) and ((a*b)%18 != 0)) or (((a+b)%18 != 0) and ((a*b)%18 == 0)):
            counter += 1
            m = max(m, a+b)
print(counter, m)