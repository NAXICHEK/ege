f = open('24.13_14643.txt').read()
f = f.replace('AXMM', ' ').split()
# f = f.replace('A', '.')
# f = f.replace('M', '.')
# f = f.replace('X', '.')
# for i in range(1000):
#     s = '.' * i
#     if f'-{s}-' in f:
#         print(i, s)
for i in f:
    print(len(i))

# МАХМАХМАХХАМХАМХХАМАМХАМ