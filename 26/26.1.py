f = open('files/26.1.txt', 'r')
first = f.readline().replace('\n', '').split()
b = []
for s in f:
    b.append(int(s))
print(first)
b.sort()
print(b)
counter = 0
summ = 0
for number in b:
    summ += number
    counter += 1
    if summ > int(first[0]):
        counter -= 1
        summ -= number
        print(number)
        break
print(counter)

