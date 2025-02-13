# r = [x for x in range(100000, 1000000) if x % 4 == 0]
# aa = []
# b = []
# for i in r:
#     a = ''
#     for j in str(i):
#         if j not in a and j != '.':
#             a = a + j
#         else:
#             a = a.replace(j, '.')
#     aa.append(a)
#     a = ''
#
#
# from itertools import product
# for x in product('02468', repeat=2):
#     s = ''.join(x)
#     b.append(s)
#
# c = 0
#
# for i in aa:
#     if '.' not in i:
#         cf = 0
#         for j in b:
#             if j in i: cf += 1
#         if cf == 0:
#             c += 1
# print(c)

from itertools import product
r, c = [str(x) for x in range(100000, 1000000, 4)], 0
aa = [i for i in r if len(set(i)) == len(i)]
b = [''.join(x) for x in product('02468', repeat=2)]
for i in aa:
    cf = 0
    for j in b:
        if j in i: cf += 1
    if cf == 0: c += 1
print(c)