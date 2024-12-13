f = open('17_6752.txt')
numbers = [int(x) for x in f]
d = []
counter = 0
m = 0
for i in range(len(numbers)):
    if numbers[i] % 3 ==0:
        m += 1
for i in range(len(numbers) - 1):
    a = numbers[i]
    b = numbers[i + 1]
    if (a > 0) or (b > 0):
        if a + b < m:
            counter += 1
            d.append(a+b)
print(counter, max(d))
