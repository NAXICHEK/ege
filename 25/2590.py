def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

for i in range(6080068, 6080176 + 1):
    if p(i):
        print(i)