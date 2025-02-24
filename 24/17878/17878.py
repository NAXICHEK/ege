from itertools import product, repeat

r = '06789'
f = open('24_17878.txt').readline()

# 1. Первоначальная замена длинных комбинаций операторов
t = []
for i in range(7, 1, -1):
    for x in product('-*', repeat=i):
        s = ''.join(x)
        t.append(s)
        f = f.replace(s, '!')

# 2. Замена нулей после операторов
replacements = [
    ('-000000', '-'), ('-00000', '-'), ('-0000', '-'), ('-000', '-'),
    ('-00', '-'), ('-0', '-'), ('*00000', '*'), ('*0000', '*'),
    ('*000', '*'), ('*00', '*'), ('*0', '*')
]
for old, new in replacements:
    f = f.replace(old, new)

# 3. Повторная замена оставшихся комбинаций операторов (ФИКС)
for i in range(7, 1, -1):
    for x in product('-*', repeat=i):
        f = f.replace(''.join(x), '!')

# 4. Фильтрация результатов
f = f.split('!')
new_f = []

for item in f:
    if not item: continue
    if all(c == '0' for c in item): continue

    if len(item) >= 2 and item[0] in '-*' and item[-1] in '-*':
        middle = item[1:-1]
        if middle.isdigit() and sum(map(int, middle)) == 0:
            continue
    new_f.append(item)

f = new_f
print(f)
m = 0
for i in f:
    try:
        m = max(m, len(i))
        if len(i) == 137:
            print('1\n'*10)
            print(i)
    except SyntaxError: pass
print(m)