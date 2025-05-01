def f(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return s
print(f(3**42 - 3**9 - 27).count('2'))
print(f'{10**42 - 10**9 - 10**3}'.count('9'))