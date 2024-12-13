def F(n):
    if n <= 10: return n
    elif n > 10 and n % 2 == 0: return 2 * F(n-2) + 6
    elif n > 10 and n % 2 == 1: return F(n-1) + 2 * n
print(F(27) - F(20))