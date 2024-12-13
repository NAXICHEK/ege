def f(c, e, s):
    if s > 5: return False
    if c == e: return True
    if c > e: return False
    return f(c + 1, e, s + 1) + f(c * 2, e, s + 1)

for i in range(4, 100):
    if not f(3, i, 0):
        print(i)
        break