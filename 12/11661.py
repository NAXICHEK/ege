for i in range(210, 300):
    s = '3' + '7' * i
    while '27' in s or '377' in s or '777' in s:
        s = s.replace('27', '32', 1)
        s = s.replace('377', '27', 1)
        s = s.replace('777', '3', 1)
    if sum(map(int, s)) % 15 == 0:
        print(i)#287