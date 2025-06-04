for i in range(3, 10001):
    s = '1' + '2' * i
    while '12' in s or '322' in s or '222' in s:
        s = s.replace('12', '2', 1)
        s = s.replace('322', '21', 1)
        s = s.replace('222', '3', 1)
    if sum(map(int, s)) == 15:
        print(i)
        break