from time import process_time

f = [0] * (1000000000000 + 2)
print(1)
for n in range(1, 100000000000):
    if n < 10: f[n] = n
    elif n % 2 == 0: f[n] = f[n%10] + f[n//10]
    else: f[n] = f[10**n] + f[n%10] - 2
c = 0
for i in f:
    if i == 0: c += 1
print(c, process_time())