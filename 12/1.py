for i in range(30):
    for j in range(30):
        for k in range(30):
            s = '0' + '1'*i + '2'*j + '3'*k + '0'
            a = s
            while '00' not in s:
                s = s.replace('01', '220', 1)
                s = s.replace('02', '1013', 1)
                s = s.replace('03', '120', 1)
            if s.count('1') == 13 and s.count('2') == 18:
                print(len(a))