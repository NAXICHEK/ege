for a in range(1000):
    count = 0
    for x in range(300):
        for y in range(300):
            if (x ** 2 - 3 * x + 2 > 0) or (y > x**2 + 7) or (x*y < a):
                count += 1
    if count == 300 * 300:
        print(a)
