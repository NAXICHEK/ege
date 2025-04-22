def f(x):
    s = ''
    while x > 0:
        s = str(x%4) + s
        x //= 4
    return s
ch = [x for x in range(10) if x % 2 == 0]
nch = [x for x in range(10) if x % 2 == 1]

for i in range(2006):
    r = f(43**56 + 113**841 - i)
    chq = 0
    nchq = 0
    for j in r:
        if int(j) in ch: chq += 1
        else: nchq += 1
    if chq % 2 == 0:
        if nchq % 2 == 0:
            if r.count('2') <= 712:
                print(i)
