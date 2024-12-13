f = open('17_17680.txt')
numbers = [int(x) for x in f]
bukwi = [str(x) for x in f]
d = []
m = []
counter = 0
for g in numbers:
    if g > 0 and g % 41 == 0:
        m.append(g)
minimal = min(m)
for i in range(len(numbers) - 1):
    a = numbers[i]
    b = numbers[i + 1]
    if a != b:
        if (a-b) % minimal == 0:
            counter += 1
            d.append(a+b)
print(counter, max(d))