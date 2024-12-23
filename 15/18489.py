# (¬ЦИФ(x,5)∧ЦИФ(x,4))→(x>A−11)
f = lambda a, b: str(a)[-1] == str(b)[-1]
m = 0
for a in range(100):
    fl = 1
    for x in range(1, 1000):
        if (((not f(x, 5)) and f(x, 4)) <= (x > (a-11))) == 0: fl = 0
    if fl:
        m = max(m, a)
print(m)