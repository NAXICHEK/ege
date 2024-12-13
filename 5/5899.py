from math import sqrt
spisokarbuzov = []

for i in range(100,1000):
    a = str(i // 100)
    b = str((i // 10) % 10)
    c = str(i % 10)
    spisokarbuzov.append(a + b)
    spisokarbuzov.append(a + b)
    spisokarbuzov.append(a + c)
    spisokarbuzov.append(b + a)
    spisokarbuzov.append(b + c)
    spisokarbuzov.append(c + a)
    spisokarbuzov.append(c + b)
    spisokarbuzov = [int(arbuzik) for arbuzik in spisokarbuzov]
    for arbuz in spisokarbuzov:
        for j in range(2, int(sqrt(arbuz)) + 1):
            if arbuz % j == 0:
                print(arbuz)

    print(spisokarbuzov)
