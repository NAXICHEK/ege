ab, ac, ba, bc, ca, cb = 0, 0, 0, 0, 0, 0
chisla = []
counter = 0
for i in range(300, 401):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a != 0:
        ab = str(a) + str(b)
        ac = str(a) + str(c)
    if b != 0:
        ba = str(b) + str(a)
        bc = str(b) + str(c)
    if c != 0:
        ca = str(c) + str(a)
        cb = str(c) + str(b)

    chisla.append(ab)
    chisla.append(ac)
    chisla.append(ba)
    chisla.append(bc)
    chisla.append(ca)
    chisla.append(cb)


    arbuz = [int(x) for x in chisla]
    if 0 in arbuz:
        g = arbuz.count(0)
        for gey in range(g):
            arbuz.remove(0)
    max1 = max(arbuz)
    min1 = min(arbuz)
    if max1 - min1 == 20:
        counter += 1
    chisla = []
    arbuz = []
print(counter)