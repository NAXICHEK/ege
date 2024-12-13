def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

for i in range(4, 10001):
    s = '3' + '7' * i
    while '37' in s or '577' in s or '777' in s:
        s = s.replace('37', '7', 1)
        s = s.replace('577', '73', 1)
        s = s.replace('777', '5', 1)
    a = sum(map(int, s))
    if p(a) == True and p(i) == True and len(str(a)) == 2 and len(str(i)) == 2:
        print(i) # 97