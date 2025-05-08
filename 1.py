from itertools import permutations
from time import process_time
n = 10
s = '>' + '0000' + '2' * 7 + '0' * 10 + '1' * n + '2'
while '>1' in s or '>2' in s or '>0' in s:
    s = s.replace('>1', '22>', 1)
    s = s.replace('>2', '2>', 1)
    s = s.replace('>0', '1>', 1)
print(n)
print(s)
print(sum(map(int, s.replace('>', ''))))
print(process_time())
