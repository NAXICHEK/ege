def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
def kr(p_cl, v_cl):
    m = 1000000000
    for i in p_cl:
        for j in v_cl:
            d = dist(i, j)
            if d != 0:
                m = min(m, d)
                # if m == 8.37466499958255:
                #     # return i, j
                # if m == 2.508894961162982:
                #     return i, j
                # if m == 3.323140540018884:
                #     return i, j
                if m == 1.5432691609933122:
                    return i, j
    return m
# f = open('27A_1_20132.txt').read().replace(',', '.').split()
f = open('27B_1_20132.txt').read().replace(',', '.').split()
g = [[float(f[x]), float(f[x+1])] for x in range(0, len(f), 2)]
pcl = []
vcl = []
tcl = []
for i in g:
    x, y = i
    # if y >= 6:
    #     pcl.append(i)
    # else: vcl.append(i)
    if (y <= 5) and (x <= 2):
        pcl.append(i)
    elif (y <= 5) and (x >= 2):
        vcl.append(i)
    else: tcl.append(i)
print(kr(vcl, tcl))
# p = [2.233081, 7.574423]
# v = [8.052613, 1.552126]
# p = [1.121883, 1.560516]
# v = [3.628501, 1.667381]

# pcl vcl ([1.121883, 1.560516], [3.628501, 1.667381])
# pcl tcl ([0.985094, 2.967868], [2.295715, 6.021642])
# vcl tcl ([4.541109, 4.52741], [4.401297, 6.064333])
# x1, y1 = p
# x2, y2 = v
# print(int((x1+x2)*10000/len(p)), int((y1+y2)*10000/len(v)))
print(int((1.121883+0.985094+4.541109+3.628501+2.295715+4.401297)*10000/6))
print(int((1.560516+2.967868+4.52741+1.667381+6.021642+6.064333)*10000/6))