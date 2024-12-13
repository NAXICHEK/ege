f = open('17.55604.txt')
a = [int(i) for i in f]
b = [str(i) for i in a]
c = []
d = []
for i in range(len(b)-1):
    if b[i][-1] == b[i][-2]:
        c.append(a[i])
minimal = min(c)
counter = 0
for i in range(len(b)-1):
    if (b[i][-1] == b[i+1][-2]) or ((b[i][-2]) == b[i+1][-1]):
        if (a[i] % 7 == 0 and a[i+1] % 7 != 0) or (a[i] % 7 != 0 and a[i+1] % 7 == 0):
            if a[i]**2 + a[i+1]**2 < minimal**2:
                d.append(a[i]**2 + a[i+1]**2)
                counter += 1
print(counter)
print(max(d))