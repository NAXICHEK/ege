from sys import set_int_max_str_digits

f = [0] * 50000
for n in range(1, 48000):
    if n < 20: f[n] = n
    elif n >= 20: f[n] = (n-6) * f[n-7]

print((f[47872] - 290 * f[47865])//f[47858])