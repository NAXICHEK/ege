# ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>0)
#   ЕСЛИ нашлось (>1)
#        ТО заменить (>1, 22>)
#   ЕСЛИ нашлось (>2)
#        ТО заменить (>2, 2>)
#   ЕСЛИ нашлось (>0)
#        ТО заменить (>0, 1>)
for i in range(3, 10000):
    s = '>' + '0' * 39 + '1' * i + '2'*39
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', "22>", 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    b = [int(g) for g in s[:-1]]
    a = sum(b)
    if a > 1 and all(a % j != 0 for j in range(2, int(a ** 0.5 + 1))):
        print(i)
        break