from time import process_time
from itertools import *
gl = []
sogl = []
c = 0
for h in product('АИЯ', repeat = 3):
    s = ''.join(h)
    gl.append(s)

for j in product('НСТ', repeat = 3):
    s = ''.join(j)
    sogl.append(s)

print(gl)
print(sogl)


for x in permutations('АНАСТАСИЯ', 9):
    s = ''.join(x)
    if not(any(y in s for y in gl) and any(y in s for y in sogl)):
        c += 1
    # fl = 1
    # # for o, p in zip(gl, sogl):
    # #     if (o in s) or (p in s):
    # #         fl = 0
    # for o in gl:
    #     for p in sogl:
    #         if o in s:
    #             if p in s:
    #                 fl = 0
    # if fl:
    #     c += 1

print(c)

# s = sorted('АНАСТАСИЯ')
# g = sorted('АИЯ')
# c = sorted('НСТ')
# count = 0
# glas = []
# soglas = []
# for d1 in g:
#     for d2 in g:
#         for d3 in g:
#             d = d1 + d2 + d3
#             glas.append(d)
#
# for f1 in g:
#     for f2 in g:
#         for f3 in g:
#             f = f1 + f2 + f3
#             soglas.append(f)
# print(glas)
# print(soglas)
# for a1 in s:
#     for a2 in s:
#         for a3 in s:
#             for a4 in s:
#                 for a5 in s:
#                     for a6 in s:
#                         for a7 in s:
#                             for a8 in s:
#                                 for a9 in s:
#                                     a = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
#                                     if a.count('А') == 3 and a.count('Н') == 1 and a.count('С') == 2 and a.count('Т') == 1 and a.count('И') == 1 and a.count('Я') == 1:
#                                         fl = 1
#                                         for p, o in zip(glas, soglas):
#                                             if p in a and o in a:
#                                                 fl = 0
#                                         if fl:
#                                             count += 1
# print(count, process_time())


# print(glas)
# print(soglas)
# print(len(glas))
#
# from itertools import *
#
# for x in set(permutations('АНАСТАСИЯ')):
#     s = ''.join(x)
#     if not(any(y in s for y in glas) and any(y in s for y in soglas)):
#         c += 1
# print(c)
