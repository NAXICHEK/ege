k = 0
p = 0
chet = '2468ace'
for a1 in '123456789abcdef':
    for a2 in '0123456789abcdef':
        for a3 in '0123456789abcdef':
            s = a1 + a2 + a3
            for i in '2468ace':
                s = s.replace(i, '1')
            for i in '3579bdf':
                s = s.replace(i, '0')
            if '00' not in s and '11' not in s:
                p += 1

            if a1 != a2 and a2 != a3 and a1 != a3:
                if (a1 in chet and a2 not in chet) or (a1 not in chet and a2 in chet) or (
                        a2 in chet and a3 not in chet) or (a2 not in chet and a3 in chet) or (
                        a1 in chet and a3 not in chet) or (a1 not in chet and a3 in chet):
                    k += 1
print(k, p)
