def func(a, x, b):
    return a <= x <= b
g = 0
for a in range(100):
    for b in range(100):
        fl = 1
        for x in range(1000):
            if not(func(15, x, 40) <= ((func(21, x, 63) and (not(a, x, b))) <= (not(15, x, 40)))):
                fl = 0
        if fl:

            print(max(a, b) - min(a, b))