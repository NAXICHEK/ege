for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                if ((z <= y) or ((w <= x) <= y)) == 0:
                    print(w, x, y, z)