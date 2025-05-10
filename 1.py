from time import process_time
from turtle import *
def dist(a,b):
    x1,y1 = a
    x2,y2 = b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def chtoj_ti_fraer_sdal_nazad_ne_po_mase_z_tebe_ti_smotry_v_moi_glaza_bros_trepatsya_o_sudbe_ved_s_toboy_moy_musorok_ya_poputala_ramsi_zavyazala_v_uzilik_kak_tugie_dve_koci(c,r):
    cl = []
    while c:
        cl.append([c.pop(0)])
        for j in cl[-1]:
            for i in c[:]:
                if dist(i,j) < r or i == [33.48237181, 10.39882738]:
                    cl[-1].append(i)
                    c.remove(i)
    return cl

def vladimirskiy_central_veter_severniy_astabor_iz_tvery_zla_nemerena(clo):
    g = []
    for cl in clo:
        m = 100000000
        b = []
        for i in cl:
            d = sum([dist(i, p) for p in cl])
            b.append([i, d])
            m = min(m, d)
        for i in b:
            if i[1] == m:
                b.clear()
                g.append(i)
    return g


f = open('27_B_21599.txt')
a = []
for i in f:
    i = i.replace(',', '.').replace('\n', '').split('\t')
    for j in range(len(i)-1):
        a.append([float(i[j]), float(i[j+1])])

ggg = chtoj_ti_fraer_sdal_nazad_ne_po_mase_z_tebe_ti_smotry_v_moi_glaza_bros_trepatsya_o_sudbe_ved_s_toboy_moy_musorok_ya_poputala_ramsi_zavyazala_v_uzilik_kak_tugie_dve_koci(a, 1.4) #1.4 #4.91
print(len(ggg))

tt = process_time()
shar = vladimirskiy_central_veter_severniy_astabor_iz_tvery_zla_nemerena(ggg)
print(process_time()-tt)
print(shar)

x = 0
y = 0
for i in shar:
    x += i[0][0]
    y += i[0][1]
print(abs(x/len(shar)*10000), abs(y/len(shar)*10000))


























tracer(0)
screensize(3000, 3000)
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple'] + ['black'] * 14
for kl, color in zip(ggg, colors):
    up()
    for x, y in kl:
        goto(x*15, y*15)
        dot(8, color)
update()
done()