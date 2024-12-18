f = open('17_14260.txt')
g = [int(x) for x in f]
m = [x for x in g if (999 < x < 10000) and x[-1] == x[-2]]
print(m) # ахуенный фаил