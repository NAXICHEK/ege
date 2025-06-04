print('w x y z')
for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                # if (((not((not x) or y)) and (not w)) or (not(z and not (y and w)))) == 0:
                #     print(w, x, y, z)
                if (not(((not x) or y) and (not w)) or (not(z and (not(y and w))))) == 0:
                    print(w, x, y, z)