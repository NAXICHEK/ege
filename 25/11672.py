from fnmatch import fnmatch
for i in range(21025, 10**10, 21025):
    if fnmatch(str(i), '12*34?5'):
        nc = 0
        ch = 0
        for j in str(i):
            if int(j) % 2 == 0: ch += 1
            else: nc += 1
        if nc == ch:
            print(i, i//21025)