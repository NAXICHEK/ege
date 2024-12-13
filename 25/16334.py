for a in range(1917, 10**10, 1917):
    a = str(a)
    if a[0] == '3':
        if a[2:4] == '12':
            if a[5:7] == '14':
                if a[-1] == '5':
                    print(a, int(a)//1917)



# a = '3?12?14*5'
# print(a[0])
# print(a[2:4])
# print(a[5:7])
# print(a[-1])