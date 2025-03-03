def d(a, b):
    return a % b == 0
def f(a, x, b):
    return a <= x <= b

for a in range(1, 100):
    t = True
    for x in range(1000):
        if (d(x, a) or (f(120, x, 180) <= ((not d(x, 16)) or (x + a <= 204)))) == 0:
            t = False
    if t:
        print(a)