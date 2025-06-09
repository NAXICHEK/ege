from string import printable

f = open('24_3163.txt').readline()
m = 0
for i in range(len(f)):
    for j in range(i+m, len(f)):
        s = f[i:j+1]
        if 'PR' not in s or 'ST' not in s:
            m = max(len(s), m)
        else:
            break
print(m)