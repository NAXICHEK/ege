from itertools import product, repeat, permutations
a = '13579b'

cc = 0
for x in product('0123456789ab', repeat=5):
    c = 0
    s = ''.join(x)
    for i in a:
        s = s.replace(i, '!')
    for i in range(len(s)-1):
        if s[i] + s[i+1] == '!!':
            c += 1
    print(s, c)
    if c <= 2:
        cc += 1
print(cc)