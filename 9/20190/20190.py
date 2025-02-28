import itertools

f = open('20190.txt')
c = 0
for s in f:
    a = sorted(set(int(x) for x in s.split()))
    if len(a) < 3:
        continue
    found = False
    for trio in itertools.combinations(a, 3):
        x, y, z = trio
        if y * y == x * z and x != y:
            found = True
            break
    if found:
        c += 1
print(c)