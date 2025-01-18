f = open('24_16333.txt').read()
f = f.replace('Q', '.')
f = f.replace('W', '.')
f = f.replace('R', '.')
f = f.replace('1', '-')
f = f.replace('2', '-')
f = f.replace('4', '-')
s = ''
g = open('24.txt', 'w').write(f)
for y in range(100):
    s += '-.'
    if s in f:
        print(len(s), s)