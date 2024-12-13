f = open('17_17873.txt')
numbers = [int(x) for x in f]
bukwi = [int(x) for x in f]
d = []
counter = 0
minimal = min(numbers)
for i in range(len(numbers) - 1 ):
    a = numbers[i]
    b = numbers[i + 1]
    if (a % 16 == minimal) or (b % 16 == minimal):
        counter += 1
        d.append(a+b)
print(counter, max(d))