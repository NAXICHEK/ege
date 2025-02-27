f = open('20190.txt')
c = 0
for s in f:
    a = [int(x) for x in s.split()]
    cc = 0
    for i in range(2, 20):
