
def div(x):
    if x > 0: return 0
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x // i}
    if len(d) > 0:
        return sorted(d)

f = open('17_6059.txt')

num = [int(s) for s in f]
c = 0
m = 0
for i in range(len(num)-1):
    a = num[i]
    b = num[i+1]
    if (a % 2 == 0) and (b % 2 == 0):
        y = div(a)
        yy = div(b)
        if (y != 0) and (yy != 0):
            mda = max(div(a))
            mdb = max(div(a))
            if (mda == mdb) and (mda+mdb > 200):
                c += 1
                m = max(m, max(mda, mdb) - min(mda, mdb))
print(c, m)