from itertools import product, repeat, permutations

a = []
for i in range(2, 10):
    for x in permutations('123456789', i):
        s = ''.join(x)
        for j in a:
            if s[::-1] == j:
                a.remove(s[::-1])
        a.append(s)
print(a)
print(len(a))