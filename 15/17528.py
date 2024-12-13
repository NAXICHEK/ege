def p(x):
    return 40 >= x >= 15

def q(x):
    return 63 >= x >= 21

def arbuz(a, b, x):
    return b >= x >= a
m = 100000
for a in range(100):
    for b in range(100):
        c = 0
        for x in range(1, 1000):
            if p(x):
                if not ((q(x) and not arbuz(a, b, x)) and p(x)):
                    c += 1
        if c == 26:
            m = min(m, b-a)
print(m)