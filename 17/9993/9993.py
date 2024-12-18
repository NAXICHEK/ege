f = open('17_9993.txt')
g = [int(x) for x in f]
m = max([x for x in g if x[-2:] == '17'])
print(m)