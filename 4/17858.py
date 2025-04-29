g = ['00', '010', '011', '1011', '1001', '1100', '1010', '1101', '111']
for i in range(1, 5):
    for j in range(2 ** i):
        a = f'{j:b}'.zfill(i)
        if all(x[:i] != a and a[:len(x)] != x for x in g):
            print(a)