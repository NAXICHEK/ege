f = open('17_14952.txt')
numbers = [int(x) for x in f]
bukwi = [str(x) for x in f]
d = []
counter = 0
m = []
vc = 0
for g in numbers:
    if str(g)[-3:] == '121':
        m.append(g)
maxx = max(m)
for i in range(len(numbers) - 2):
    vc = 0
    a = numbers[i]
    b = numbers[i + 1]
    c = numbers[i + 2]
    if ((a > 999) or (a < -999)) and (a % 2 == 0):
        vc += 1
    if ((b > 999) or (b < -999)) and (b % 2 == 0):
        vc += 1
    if ((c > 999) or (c < -999)) and (c % 2 == 0):
        vc += 1
    if (vc == 0) or (vc == 1):
        if a+b+c <= maxx:
            counter += 1
            d.append(a+b+c)
print(counter, max(d))