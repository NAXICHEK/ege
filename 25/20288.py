from fnmatch import fnmatch
for i in range(9231, 10**10 + 1, 9231):
    t = True
    a = []
    for j in str(i)[:-5]:
        a.append(j)
    if fnmatch(str(i), '*12?4?'):
        for h in a:
            if int(h) % 2 != 0: t = False
        if t and str(i)[-3] in '13579' and str(i)[-1] in '13579':
            print(i, i//9231)

# *12?4?
# a = '812848'
# print(a[-5:-3])
# print(a[-2:-1])
# print(a[-1])
# print(a[-3])
#
# for i in range(9231, 10**10):
#     i = str(i)
#     if i[-5:-3] == '12':
#         if i[-2:-1] == '4':
#             if i[-1] in '0123456789':
#                 if i[-3] in '0123456789':
#                     if int(i) % 9231 == 0:
#                         print(i, int(i)//9231)