from os import write

f = open('24_3163.txt').read()
l = f
f = f.replace('PR', '!').replace('ST', '@')
c = 0
f = f.split('@')
for i in f:
    if '!' in f:
        f.remove(i)
    if len(i) == 6570:
        print(i)
        r = open('123', 'w').write(i)
g = []
for i in f:
    g.append(len(i))
print(max(g))