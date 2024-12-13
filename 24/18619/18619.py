f = open('24_18619.txt')
numbers = [str(x) for x in f]
numbers = str(numbers)
numbers = numbers.replace('[', '')
numbers = numbers.replace(']', '')
numbers = numbers.replace("'", '')
d = []
for a in numbers:
    d.append(a)
