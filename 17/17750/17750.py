f = open('17_17750.txt')
numbers = [int(x) for x in f]
bukwi = [str(x) for x in f]
d = []
counter = 0
for i in range(len(numbers) - 1):
    a = numbers[i]
    b = numbers[i + 1]
    if (a % 77) + (b % 77) == min(numbers):
        counter += 1
        d.append(a+b)
print(counter, max(d))