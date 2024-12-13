def f(x, y):
    return x % y == 0

for a in range(1, 1000):
    c = 0
    for x in range(1, 1000):
        if f(x, 15) and (not(f(x, 10))) <= (a < (x + 50)):
            c += 1
    if c == 1000:
        print(x)