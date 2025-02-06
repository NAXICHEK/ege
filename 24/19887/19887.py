f = open('24.23_19887.txt').readline()
c = 0
a1 = []
a2 = []
for i in f:
    if (int(i) % 2 == 0) and (c <= 10000) and ((i != '.') or (i != '-')):
        f = f.replace(i, '.')
        c += 1
    elif (int(i) % 2 != 0) and (c <= 10000) and ((i != '.') or (i != '-')):
        f = f.replace(i, '-')
        c += 1
    else: pass
g = open('123', 'w').write(f)
for i in range(1000):
    s = '.-' * i
    if s in f:
        a1.append([len(s), s])
    s = '-.' * i
    if s in f:
        a2.append([len(s), s])
a = a1 + a2
print(a)