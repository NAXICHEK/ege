from itertools import product, repeat, count
# c = 0
# a = set()
# for x in product('024', repeat=3):
#     s = ''.join(x)
#     a.add(s)
# for x in product('01234', repeat=9):
#     s = ''.join(x)
#     t = True
#     if s[0] != '0':
#         if s.count('02') + s.count('20') + s.count('24') + s.count('42') + s.count('04') + s.count('40') == 2:
#             for i in a:
#                 if i in s:
#                     t = False
#             if t:
#                 c += 1
# print(c)

c = 0
for x in product('01234', repeat=9):
    s = ''.join(x)
    if s[0] != '0':
        s = s.replace('0', '!').replace('2', '!').replace('4', '!')
        if s.count('!!') == 2 and '!!!' not in s:
            c +=1
print(c)