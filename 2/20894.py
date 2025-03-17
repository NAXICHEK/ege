print('w x y z')
for w in 0, 1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                if 0 == ((not (x <= y)) or (z <= w) or (not z)):
                    print(w, x, y, z)