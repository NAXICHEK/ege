print('w x y z f')
for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                print(w, x, y, z, 1 if x and ((w <= y) == z) else 0)