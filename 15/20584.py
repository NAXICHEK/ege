

for a in range(1000):
    t = True
    for x in range(1, 1000):
        if (((405%x==0) <= (81%x==0)) or (a - x > 162)) == 0:
            t = False
    if t:
        print(a)
        break