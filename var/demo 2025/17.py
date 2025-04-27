f = open('17_17873.txt'); g = [int(x) for x in f]; c = 0; minimal = min(g); m = 0
for i in range(len(g)-1):
    a = g[i]; b = g[i+1]
    if (a % 16 == minimal) or (b % 16 == minimal): c += 1; m = max(m, a+b)
print(c, m)