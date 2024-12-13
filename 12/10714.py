m = 0
for i in range(4, 10001):
    s = '1' + '2' * i
    while '12' in s or '322' in s or '222' in s:
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s .replace('222', '3', 1)
    m = max(m, len(s))
    print(m)#9