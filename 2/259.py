print('x y z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if 1 == ((x <= y) and (y <= z)):
                print(x, y, z)