for a in range(1, 150):
    c = 0
    for x in range(1, 151):
        for y in range(1, 151):
            if (x + y <= 30) or (y <= x+2) or (y>=a):
                c += 1
    if c == 22500:
        print(a)
def d(x, y):
    return x % y == 0
print(d(5, 2))