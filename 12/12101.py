for i in range(4, 10000):
    s = '9' + '4' * i
    a = s.count('4')
    while '94' in s or '644' in s or '444' in s:
        s = s.replace('94', '4', 1)
        s = s.replace('644', '49', 1)
        s = s.replace('444', '6', 1)
    if s.count('4') * 18 == a:
        print(i)