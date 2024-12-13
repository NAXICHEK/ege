print("wxyz")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if 0 == ((x and (not y)) or (x == z) or w):
                    print(w, x, y, z)