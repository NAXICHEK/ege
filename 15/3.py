def dell(x, y):
    return x % y == 0

for a in range(1, 1000):
    c = 0
    for x in range(1, 1000):
        if (dell(x, 2) <= (not(dell(x, 3)))) or ((x + a) >= 100):
            c += 1
    if c == 1000:
        print(a)