from sys import setrecursionlimit
setrecursionlimit(9999)
def f(n):
    for x in range(1000):
        if n >= 3000:
            return n
        if n < 3000:
            return n + 12 + f(n+2)
print(f(2984) - f(2988))

# # print(f())
# for x in range(-100, 100):
#     f = [0] * 3003
#     for n in range(3002, 1, -1):
#         if n >= 3000:
#             f[n] = n
#         else:
#             f[n] = n + x + f[n + 2]
#     if f[2984] - f[2988] == 5916:
#         print(x)
#         break