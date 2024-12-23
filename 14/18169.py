from time import process_time


def f(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s

for x in range(1, 100000):
    r = f(3**2000 + 3**10 - x)
    if r.count('2') == 2000:
        print(x,r.count('2'), process_time())