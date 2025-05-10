from time import process_time
d = 0
f = [0] * 500000010
for n in range(1, 500000001):
    f[0] = 1
    if n > 0 and n % 2 != 0:
        f[n] = 1 + f[n-1]
    else:
        f[n] = f[n//2]
    if f[n] == 3: d += 1; print(d)
print(d, process_time())