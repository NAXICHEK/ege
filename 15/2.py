def f(a, b, x):
    return b >= x >= a

for a in range(100):
    for b in range(100):
        c = 0
        for x in range(1000):
            if (not((f(32, 68, x)) or (f(54, 76, x)))) == (not(f(a, b, x))):
                c += 1
        if c == 1000:
            print(b-a)