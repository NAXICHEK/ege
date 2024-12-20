a = [1, 2, 3, 4, 5]
for i in range(len(a)-1):
    for j in (i+1, len(a)):
        print(i, j)