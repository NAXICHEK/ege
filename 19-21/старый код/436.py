def f(a,b,m):
    if a+b >= 44: return m % 2 == 0
    if m == 0: return 0
    h = [
        f(a+b, b, m-1),
        f(a,a+b,m-1)
    ]
    return any(h) if (m-1) % 2 == 0 else all(h)
m = 0
q = []
w = []
e = []
print('19)', [s for s in range(1, 1000) if f(11, s, 1)]) # 17
print('20)', [s for s in range(1, 1000) if f(11, s, 2)]) # 8
for i in range(1, 100):
    for j in range(1, 100):
        if f(i, j, 3):
            print(i, j)
            # if i == j:
            #     print(i, j) # 7 7 (верный ответ)