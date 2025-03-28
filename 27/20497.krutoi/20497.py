f = open('27.19.A_20497-2.txt')
g = [x[:-1].replace(',', '.').split() for x in f]

def centr(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def sistema_poiska_centroidov_ak47(cluster):
    rasstoyaniya = []
    for i in cluster:
        r = 0
        for j in cluster:
            d = centr(i, j)
            if d != 0:
                r += d
        rasstoyaniya.append([i, r])
    m = 100000000000
    for i in rasstoyaniya:
        m = min(m, i[1])
    for i in rasstoyaniya:
        if i[1] == m:
            otv_x.append(i[0][0])
            otv_y.append(i[0][1])
otv_x = []
otv_y = []
anom = []
pc = []
vc = []
tc = []
for x, y in g:
    x = float(x)
    y = float(y)
    if (1.2 < y < 6) and (-1 < x < 1.6):
        pc.append([x, y])
    elif (-4.8 < y < 0.2) and (-2.8 < x < -0.2):
        vc.append([x, y])
    elif (0.6 < x < 3.2) and (-5.2 < y < 0.4):
        tc.append([x, y])
    else:
        anom.append([x, y])
sistema_poiska_centroidov_ak47(pc)
sistema_poiska_centroidov_ak47(vc)
sistema_poiska_centroidov_ak47(tc)
print(sum(otv_x)/len(otv_x)*10000)
print(sum(otv_y)/len(otv_y)*10000)