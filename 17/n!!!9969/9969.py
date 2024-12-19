from itertools import *
f = open('17_9969.txt')
g = [int(x) for x in f]
unic = []
maxi_for_u = 0
m = 0
counter = 0

for j in g:
    j = str(abs(j))
    d = set(x for x in j)
    unic.append([j, len(d)])

# for i in unic:
#     maxi_for_u = max(maxi_for_u, i[1])
#     m = max(m, int(i[0]) if i[1] == maxi_for_u else m)
# print(m) # кайф 👍

for i in unic:
    maxi_for_u = max(maxi_for_u, i[1])

for i in unic:
    if i[1] == maxi_for_u:
        m = max(m, int(i[0]))

# def meshanina(x):
#     d = []
#     ss = ''
#     for j in x:
#         ss = ss + str(j)
#     for x in permutations(ss):
#         s = ''.join(x)
#         d.append(s)
#     return d

def meshanina(x):
    result = list(permutations(x))
    return [list(item) for item in result]

maxx = 0
a = []
for i in range(len(g)-2):
    a.append([g[i], g[i+1], g[i+2]])
        # if l[0] >= 0 and l[0] ** 0.5 % 1 == 0:
    for q in meshanina(a):
        if q[0][0] >= 0 and q[0][0] ** 0.5 % 1 == 0:
            if q[0][1] + q[0][2] > m:
                counter += 1
                maxx = max(maxx, q[0][1] * q[0][2])
    a.clear()
print(counter)
print(maxx)