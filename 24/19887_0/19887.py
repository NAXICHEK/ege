from re import *
f = open('24.23_19887.txt').read()
for i in range(10):
    if i % 2 == 0:
        f = f.replace(f'{i}', '!')
    else:
        f = f.replace(f'{i}', '?')

reg = r'(\?!)+!?|(!\?)+?'

print(max([len(x.group()) for x in finditer(reg, f)]))