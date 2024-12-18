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
print(maxi_for_u)
for i in unic:
    if i[1] == maxi_for_u:
        m = max(m, int(i[0]))
print(m)

for i in range(len(g)-2):
    a = g[i]
    b = g[i+1]
    c = g[i+2]
    if ((a**2 % a == 0 if a != 0 else False) and (b + c >= m)) or ((b**2 % b == 0 if b != 0 else False) and (a + c >= m)) or ((c**2 % c == 0 if c != 0 else False) and (b + a >= m)):
        counter += 1
print(counter)