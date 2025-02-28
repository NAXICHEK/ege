from itertools import combinations

from aiogram.utils.markdown import blockquote

a = [1, 2, 3, 4, 5, 6]
for x in combinations(a, 3):
    print(x)