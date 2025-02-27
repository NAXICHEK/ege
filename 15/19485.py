def f(x):
    b = 170 <= x <= 220
    return (x % a == 0) or (b <= (x % 24 != 0))

c = 0
for i in range(100):
    if all(f(x)) == 1: for x in range(1000)