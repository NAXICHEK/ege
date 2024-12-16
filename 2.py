c = 0
maxi = 0
for i in range(1100, 11000+1):
    if (i % 6 == 0) and (i % 7 != 0) and (i % 13 != 0) and (i % 17 != 0) and (i % 23 != 0):
        c += 1
        maxi = max(maxi, i)
print(c, maxi)