a = []

def f(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s

for n in range(1, 1000):
    b = f(n)
    if n % 3 == 0:
        b = b + b[-2:]
    else:
        b = b + f(sum(map(int, b)))
    r = int(b, 3)
    if r > 220:
        a.append(r)
print(min(a))