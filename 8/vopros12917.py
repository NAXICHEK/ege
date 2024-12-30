# from itertools import *
# c = 0
# for x in permutations('ПРОСТО', 6):
#     s = ''.join(x)
#     print(s)
#     c += 1
# print(c)

c = 0
for b1 in 'ПРОСТ':
    for b2 in 'ПРОСТ':
        for b3 in 'ПРОСТ':
            for b4 in 'ПРОСТ':
                for b5 in 'ПРОСТ':
                    for b6 in 'ПРОСТ':
                        s = b1 + b2 + b3 + b4 + b5 + b6
                        if s.count('П') == 1 and s.count('Р') == 1 and s.count('С') == 1 and s.count('О') == 2 and s.count('Т') == 1:
                            c += 1
print(c)