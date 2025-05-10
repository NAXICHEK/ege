from time import process_time
          1000000000
f = [0] * 1000000010
f[0] = 6
for n in range(1, 1000000002):
    if n > 0 and n % 2 == 0: f[n] = 1 + f[n//2]
    else: f[n] = f[n//2]

c = 0
for i in f:
    if i == 9: c += 1; print(c)
print(c, process_time())