for i, j in zip([int(i) for i in range(-999, 1)], [int(i) for i in range(999, 1, -1)]):
    if j % 1 == 0:
        print(i%13, j%13, i, j)