from itertools import *
def f1(x, y,w, z):
    return (w==x) and (y<=z)
def f2(x,y,w, z) :
    return (w<=x)<=(y==z)


for a1 in 0,1:
    for a2 in 0,1:
        for a3 in 0,1:
            for a4 in 0,1:
                t = [ [1, a1, 1, 1], [a2, 1,0, 0], [a3, 0, 0, a4]]
                c = 0
                for g in t:
                    if f1(g[0], g[1], g[2], g[3]) and c <3:
                        c += 1
                        print(a1, a2, a3, a4)