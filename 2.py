def f(x):
    s = ''
    while x > 0:
        s = str(x%3) + s
        x //= 3
    return s
for i in range(-100000, 100000):
    if f(i).count('2') == 10:
        print(i)
print(f(59050))
print(f(3**2000 + 3**10 - 59050).count('2'))
# 3**2000-3**10-5904