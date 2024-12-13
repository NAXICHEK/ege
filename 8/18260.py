
c = 0
s = '0123456789AB'
for a1 in '123456789AB':
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    for a6 in s:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        ch = a.count('0') + a.count('2') + a.count('4') + a.count('6') + a.count('8') + a.count('A')
                        nch = a.count('1') + a.count('3') + a.count('5') + a.count('7') + a.count('9') + a.count('B')
                        if (ch == nch) and (a.count("B") == 1):
                            c += 1
print(c) # 297000








# c = 0
# s = '0123456789AB'
# for a1 in '123456789AB':
#     for a2 in s:
#         for a3 in s:
#             for a4 in s:
#                 for a5 in s:
#                     for a6 in s:
#                         a = a1 + a2 + a3 + a4 + a5 + a6
#                         if a.count('B') == 1:
#                             g = 0
#                             h = 0
#                             for ads in a:
#                                 if ads == 'A':
#                                     g += 1
#                                     pass
#                                 if ads == 'B':
#                                     h += 1
#                                     pass
#                                 if type(ads) == int:
#                                     ads = int(ads)
#                                     if ads % 2 == 0:
#                                         g += 1
#                                     else:
#                                         h += 1
#                                     if h == g:
#                                         c += 1
# print(c)
