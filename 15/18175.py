def f(x, y):
    return x % y == 0

for a in range(1, 100):
    fl = 1
    for x in range(1 ,1000):
        if not((not(f(x, 7)) and f(x, 13)) <= (x > (a - 40))):
            fl = 0
    if fl:
        print(a) # 52