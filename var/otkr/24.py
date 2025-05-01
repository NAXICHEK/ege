f = open('24_21908.txt').read()
d = 0
for i in f:
    if i not in '0123456789!ABCD':
        f = f.replace(i, '!').replace('F', '!')
        d += 1
    if d == 100:
        break
for i in range(50, 1, -1):
    s = '!' * i
    if s in f:
        f = f.replace(s, '!')
f = f.split('!')
qq = []
for i in f:
    if i:
        sa = int(i, 14)
        if sa % 2 == 0:
            qq.append(sa)
m = 0
for i in qq:
    m = max(len(str(i)), m)
print(m)