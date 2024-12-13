print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x == (not z)) <= ((x or w) == y)) == 0:
                    print(x, y, z, w)
                    # с августа меня штормит меня качает