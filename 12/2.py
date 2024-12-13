a = []
b = []
for i in range(200, 300):
    s = '1' * i
    while '1111' in s:
        s = s.replace('1111', '2', 1)
        s = s.replace('222', '1', 1)
    a.append(s.count('1'))
    b.append(i)
print(b[a.index(max(a))])