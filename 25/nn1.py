for i in range (18782, 18823):
    d = []
    for j in range(2, i):
        if i % j == 0 and j % 2 != 0:
            d.append(j)
    if len(d) == 3:
        print(d[0], d[1], d[2])