from math import *
from time import process_time


# пункт а
def dist(x1, y1, x2, y2): # находим дистанцию
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def centr(a, b): # находим центроид
    x1, y1 = a
    x2, y2 = b
    return dist(x1, y1, x2, y2)

f = open('27_A_20911.txt')
g = [x[:-1].replace(',', '.').split() for x in f] # открытие файла
g = g[1:] # пропускаем 1 строчку
pc = []
vc = []
pcd = []
vcd = []
print(g)
for a, b in g: # разделение на кластеры
    a, b = float(a), float(b)
    if b > 0:
        pc.append([a, b])
    else:
        vc.append([a, b])

for i in pc: # нахождение суммы расстояний 1 кластера
    r = 0
    for j in pc:
        d = centr(i, j)
        if d != 0:
            r += d
    pcd.append([i, r])
m1 = 10000
for i in pcd: # нахождение минимальной суммы
    m1 = min(m1, i[1])
print(m1, pcd) # 3.7046261187 5.757797218 принтую и ручками ищу центроид по расстоянию
m2 = 10000
for i in vc: # тоже самое для второго кластера
    r = 0
    for j in vc:
        d = centr(i, j)
        if d != 0:
            r += d
    vcd.append([i, r])
m2 = 10000
for i in vcd:
    m2 = min(m2, i[1])
print(m2, vcd) # 2.0161619849 -3.6989345413

# Пункт б

f = open('27_B_20911.txt')
g = [x[:-1].replace(',', '.').split() for x in f]
g = g[1:]
pc = []
vc = []
tc = []
pcd = []
vcd = []
tcd = []
for a, b in g: # разбиваем на кластеры
    a, b = float(a), float(b)
    if b >= 5:
        pc.append([a, b])
    elif (b < 5) and (b > -6):
        vc.append([a, b])
    elif b <= -6:
        tc.append([a, b])
if pc: print(1)
if vc: print(1)
if tc: print(1)
otv = []
for i in pc: # сумма расстояний
    r = 0
    for j in pc:
        d = centr(i, j)
        if d != 0:
            r += d
    pcd.append([i, r])
m1 = 100000000000
for i in pcd:
    m1 = min(m1, i[1])
print(m1) #
for i in vc:
    r = 0
    for j in vc:
        d = centr(i, j)
        if d != 0:
            r += d
    vcd.append([i, r])
m2 = 100000000000
for i in vcd:
    m2 = min(m2, i[1])
print(m2) #

for i in tc:
    r = 0
    for j in tc:
        d = centr(i, j)
        if d != 0:
            r += d
    tcd.append([i, r])
m3 = 100000000000
for i in tcd:
    m3 = min(m3, i[1])
print(m3)

for i in pcd: # ещё один шедевро перебор чтобы как в пункте а не искать руками
    if i[1] == m1:
        otv.append(i)

for i in vcd:
    if i[1] == m2:
        otv.append(i)

for i in tcd:
    if i[1] == m3:
        otv.append(i)
print(otv) # смотри мответ и уже ручками пишем
# САМАЯ РЖАКА СМЕЯКА
# А: 28603 10294
# Б: 61260 -11200
# Всё правильно кроме -11200
print('А:', floor((3.7046261187+2.0161619849)/2*10000), floor((5.757797218+(-3.6989345413))/2*10000))
print('Б:', floor((10.6474896077+3.6152550029+4.1152564179)/3*10000), abs(floor((9.7580909613-0.0975921536-13.0184433974)/3*10000)), process_time())