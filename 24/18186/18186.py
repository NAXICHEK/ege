f = open('24_18186.txt').readline()
gl = 'AEIOUY'
sogl = 'BCDFGHJKLMNPQRSTVWXZ'
m = 0
gl1 = 0
sogl1 = 0
for i in f:
    if i in gl and gl1 <= 6:
        f = f.replace(i, '-')
        gl1 += 1
    elif i in sogl and sogl1 <= 20:
        f = f.replace(i, '.')
        sogl1 += 1
# ИЛИ
f = f.replace('..-', ' ').split()
for i in f:
    m = max(len(i), m)
print(m+6)
# ИЛИ
# f = f.replace('..-', '1')
# f = f.replace('-', '.')
# for i in range(100):
#     a = '1' + '.' * i + '1'
#     if a in f:
#         m = max(a.count('.'), m)
# print(m+6)