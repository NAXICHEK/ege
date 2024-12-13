import time
def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)
a = []
for i in range(525784203, 728943762 + 1):
    d = div(i)
    if len(d) == 3:
        a.append(i)
        a.append(d[2])
        print(i, time.process_time())
print(a, time.process_time())