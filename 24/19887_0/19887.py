from re import *
f = open('24.23_19887.txt').read()
print(f)
# for i in range(10):
#     if i % 2 == 0:
#         f = f.replace(f'{i}', '!')
#     elif i % 2 != 0:
#         f = f.replace(f'{i}', '?')
#     else:
#         f = f.replace(f'{i}', '@')
# reg = r'(?!|!?)+'
reg = r'([02468]|[13579])+'
print(x.group() for x in finditer(reg, f))